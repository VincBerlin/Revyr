import re, json, os
_REPO = os.environ.get("REVYR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG=os.path.join(_REPO, "docs/ID-REGISTRY.md")
CAN=os.path.join(_REPO, "docs/canvas/revyr-endurance-platform.canvas.md")
def cells(l): return [c.strip() for c in l.strip().strip("|").split("|")]

reg={}
for raw in open(REG,encoding="utf-8"):
    if raw.strip().startswith("|"):
        c=cells(raw)
        if len(c)>=9 and re.fullmatch(r'CAN-\d{3}',c[0]) and '`docs/canvas' in c[3]:
            st=c[4].replace("*","").strip()
            reg[c[0]]=st
act={k for k,v in reg.items() if v=="active"}
dep={k for k,v in reg.items() if v=="deprecated"}
res={k for k,v in reg.items() if v=="reserved"}

lines=open(CAN,encoding="utf-8").read().split("\n")
DEF=["ID","Aussage","Source Type","Source","Herkunft","Befund / Hinweis"]
RES=["ID","Fehlende Aussage","Herkunft","Wer hängt daran","Warum nicht ableitbar"]
canvas_def,canvas_res=set(),set()
i=0
while i<len(lines):
    if lines[i].strip().startswith("|"):
        blk=[]
        while i<len(lines) and lines[i].strip().startswith("|"): blk.append(lines[i]); i+=1
        h=cells(blk[0])
        tgt = canvas_def if h==DEF else (canvas_res if h==RES else None)
        if tgt is not None:
            for r in blk[2:]:
                c=cells(r)
                if re.fullmatch(r'CAN-\d{3}',c[0]): tgt.add(c[0])
    else: i+=1

print(json.dumps({
 "registry_active": len(act), "registry_deprecated": len(dep), "registry_reserved": len(res),
 "canvas_definition_rows": len(canvas_def), "canvas_reserved_rows": len(canvas_res),
 "active_in_registry_missing_from_canvas": sorted(act-canvas_def),
 "in_canvas_but_not_active_in_registry": sorted(canvas_def-act),
 "reserved_mismatch": sorted(res^canvas_res),
 "deprecated_leaking_into_canvas_defs": sorted(dep&canvas_def),
}, ensure_ascii=False, indent=2))
