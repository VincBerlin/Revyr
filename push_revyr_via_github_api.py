#!/usr/bin/env python3
"""
Upload the current REVYR project to GitHub without using `git push`.

Usage:
  python3 push_revyr_via_github_api.py "$HOME/Documents/Revyr-clean"

Requirements:
  - GitHub CLI (`gh`) installed
  - `gh auth status` succeeds
  - Repository VincBerlin/Revyr already exists
"""

from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

REPOSITORY = "VincBerlin/Revyr"
BRANCH = "main"
REMOTE_URL = f"https://github.com/{REPOSITORY}.git"
MAX_BLOB_BYTES = 95 * 1024 * 1024


def run(
    args: list[str],
    *,
    cwd: Path,
    payload: dict[str, Any] | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    input_text = json.dumps(payload, ensure_ascii=False) if payload is not None else None
    result = subprocess.run(
        args,
        cwd=str(cwd),
        input=input_text,
        text=True,
        capture_output=True,
    )
    if check and result.returncode != 0:
        print(f"\nFEHLER bei: {' '.join(args)}", file=sys.stderr)
        if result.stdout.strip():
            print(result.stdout, file=sys.stderr)
        if result.stderr.strip():
            print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    return result


def gh_api(
    endpoint: str,
    *,
    cwd: Path,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
    check: bool = True,
) -> tuple[subprocess.CompletedProcess[str], dict[str, Any] | None]:
    args = ["gh", "api", endpoint]
    if method != "GET":
        args += ["--method", method]
    if payload is not None:
        args += ["--input", "-"]
    result = run(args, cwd=cwd, payload=payload, check=check)
    parsed = None
    if result.stdout.strip():
        try:
            parsed = json.loads(result.stdout)
        except json.JSONDecodeError:
            parsed = None
    return result, parsed


def ensure_git_repo(project: Path) -> None:
    if not (project / ".git").exists():
        run(["git", "init", "-b", BRANCH], cwd=project)
    else:
        current = run(
            ["git", "branch", "--show-current"],
            cwd=project,
            check=False,
        ).stdout.strip()
        if not current:
            run(["git", "switch", "-C", BRANCH], cwd=project)
        elif current != BRANCH:
            print(f"Hinweis: Aktueller Branch ist {current!r}; Upload erfolgt nach GitHub/{BRANCH}.")

    remote = run(["git", "remote", "get-url", "origin"], cwd=project, check=False)
    if remote.returncode == 0:
        run(["git", "remote", "set-url", "origin", REMOTE_URL], cwd=project)
    else:
        run(["git", "remote", "add", "origin", REMOTE_URL], cwd=project)


def staged_files(project: Path) -> list[tuple[str, str]]:
    run(["git", "add", "-A"], cwd=project)
    result = run(["git", "ls-files", "-s", "-z"], cwd=project)
    entries: list[tuple[str, str]] = []

    for raw in result.stdout.split("\0"):
        if not raw:
            continue
        metadata, path = raw.split("\t", 1)
        mode, _blob_sha, stage = metadata.split()
        if stage != "0":
            raise SystemExit(f"Nicht aufgelöster Index-Eintrag: {path}")
        if mode == "160000":
            raise SystemExit(
                f"Submodule nicht unterstützt: {path}. "
                "Bitte zuerst als normale Dateien übernehmen oder separat behandeln."
            )
        entries.append((mode, path))

    if not entries:
        raise SystemExit("Keine Dateien zum Hochladen gefunden.")

    return entries


def read_git_content(project: Path, mode: str, rel_path: str) -> bytes:
    path = project / rel_path
    if mode == "120000":
        return os.readlink(path).encode("utf-8")
    return path.read_bytes()


def main() -> int:
    if len(sys.argv) != 2:
        print('Aufruf: python3 push_revyr_via_github_api.py "$HOME/Documents/Revyr-clean"')
        return 2

    project = Path(os.path.expandvars(os.path.expanduser(sys.argv[1]))).resolve()
    if not project.is_dir():
        print(f"Projektordner nicht gefunden: {project}", file=sys.stderr)
        return 2

    print(f"Projekt: {project}")
    print(f"GitHub:  {REPOSITORY}")
    print("Methode: GitHub Git Data API (umgeht den fehlerhaften git-push-Transport)\n")

    run(["gh", "auth", "status"], cwd=project)
    gh_api(f"repos/{REPOSITORY}", cwd=project)
    ensure_git_repo(project)
    files = staged_files(project)

    oversized: list[str] = []
    total_bytes = 0
    for mode, rel_path in files:
        data = read_git_content(project, mode, rel_path)
        total_bytes += len(data)
        if len(data) > MAX_BLOB_BYTES:
            oversized.append(f"{rel_path} ({len(data)} Bytes)")

    if oversized:
        print("Diese Dateien überschreiten das sichere GitHub-Limit:", file=sys.stderr)
        for item in oversized:
            print(f"- {item}", file=sys.stderr)
        return 3

    print(f"Dateien: {len(files)}")
    print(f"Datenmenge: {total_bytes / 1024 / 1024:.2f} MiB")
    print("\n1/4 GitHub-Basis prüfen …")

    ref_result, ref_data = gh_api(
        f"repos/{REPOSITORY}/git/ref/heads/{BRANCH}",
        cwd=project,
        check=False,
    )

    parent_sha: str | None = None
    base_tree_sha: str | None = None

    if ref_result.returncode == 0 and ref_data:
        parent_sha = ref_data["object"]["sha"]
        _, commit_data = gh_api(
            f"repos/{REPOSITORY}/git/commits/{parent_sha}",
            cwd=project,
        )
        if not commit_data:
            raise SystemExit("Bestehender GitHub-Commit konnte nicht gelesen werden.")
        base_tree_sha = commit_data["tree"]["sha"]
        print(f"Bestehender main-Commit: {parent_sha[:12]}")
    else:
        print("Repository ist leer. Erster main-Commit wird angelegt.")

    print("\n2/4 Dateien als Git-Blobs hochladen …")
    tree_entries: list[dict[str, str]] = []

    for index, (mode, rel_path) in enumerate(files, start=1):
        content = read_git_content(project, mode, rel_path)
        _, blob_data = gh_api(
            f"repos/{REPOSITORY}/git/blobs",
            cwd=project,
            method="POST",
            payload={
                "content": base64.b64encode(content).decode("ascii"),
                "encoding": "base64",
            },
        )
        if not blob_data or "sha" not in blob_data:
            raise SystemExit(f"Blob-Upload ohne SHA: {rel_path}")

        tree_entries.append(
            {
                "path": rel_path,
                "mode": mode,
                "type": "blob",
                "sha": blob_data["sha"],
            }
        )
        print(f"[{index:>3}/{len(files)}] {rel_path}")

    print("\n3/4 Tree und Commit erstellen …")
    tree_payload: dict[str, Any] = {"tree": tree_entries}
    if base_tree_sha:
        tree_payload["base_tree"] = base_tree_sha

    _, tree_data = gh_api(
        f"repos/{REPOSITORY}/git/trees",
        cwd=project,
        method="POST",
        payload=tree_payload,
    )
    if not tree_data or "sha" not in tree_data:
        raise SystemExit("GitHub-Tree konnte nicht erstellt werden.")

    commit_payload: dict[str, Any] = {
        "message": "chore: restore REVYR and continue Plumbline baseline",
        "tree": tree_data["sha"],
        "parents": [parent_sha] if parent_sha else [],
    }
    _, commit_data = gh_api(
        f"repos/{REPOSITORY}/git/commits",
        cwd=project,
        method="POST",
        payload=commit_payload,
    )
    if not commit_data or "sha" not in commit_data:
        raise SystemExit("GitHub-Commit konnte nicht erstellt werden.")

    commit_sha = commit_data["sha"]

    if parent_sha:
        gh_api(
            f"repos/{REPOSITORY}/git/refs/heads/{BRANCH}",
            cwd=project,
            method="PATCH",
            payload={"sha": commit_sha, "force": False},
        )
    else:
        gh_api(
            f"repos/{REPOSITORY}/git/refs",
            cwd=project,
            method="POST",
            payload={"ref": f"refs/heads/{BRANCH}", "sha": commit_sha},
        )

    print(f"GitHub-Commit erstellt: {commit_sha}")

    print("\n4/4 Remote prüfen und lokale Git-Basis synchronisieren …")
    _, verify_data = gh_api(
        f"repos/{REPOSITORY}/commits/{BRANCH}",
        cwd=project,
    )
    if not verify_data or verify_data.get("sha") != commit_sha:
        raise SystemExit("Remote-Verifikation ist fehlgeschlagen.")

    fetch = run(
        ["git", "fetch", "--depth=1", "origin", BRANCH],
        cwd=project,
        check=False,
    )
    if fetch.returncode == 0:
        run(["git", "switch", "-C", BRANCH], cwd=project)
        run(["git", "reset", "--mixed", f"origin/{BRANCH}"], cwd=project)
        run(
            ["git", "branch", "--set-upstream-to", f"origin/{BRANCH}", BRANCH],
            cwd=project,
            check=False,
        )
        print("Lokaler main-Branch wurde mit origin/main synchronisiert.")
    else:
        print(
            "GitHub ist vollständig befüllt. Der anschließende lokale Fetch wurde "
            "durch die bekannte Verbindung gestört; das betrifft den Remote-Upload nicht."
        )

    print("\nERFOLG")
    print(f"Repository: https://github.com/{REPOSITORY}")
    print(f"Commit:     {commit_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
