// mobile/src/ui/__tests__/ErrorBoundary.test.tsx
import React from 'react';
import TestRenderer, { act } from 'react-test-renderer';
import { Text } from 'react-native';
import { ErrorBoundary } from '../ErrorBoundary';

function InnerText(props: { text: string }): React.JSX.Element {
  return <Text>{props.text}</Text>;
}

function Boom(): React.JSX.Element {
  throw new Error('BOOM');
}

describe('ErrorBoundary', () => {
  test('rendert Children ohne Fehler durch', () => {
    const tree = TestRenderer.create(
      <ErrorBoundary>
        <InnerText text="hallo" />
      </ErrorBoundary>,
    );
    const rendered = JSON.stringify(tree.toJSON());
    expect(rendered).toContain('hallo');
    tree.unmount();
  });

  test('faengt Renderer-Fehler und zeigt Fallback mit Nachricht', () => {
    // React 19 loggt Fehler in ErrorBoundaries an console.error; hier stumm halten.
    const errSpy = jest.spyOn(console, 'error').mockImplementation((): void => undefined);
    const onError = jest.fn();
    const tree = TestRenderer.create(
      <ErrorBoundary onError={onError}>
        <Boom />
      </ErrorBoundary>,
    );
    const rendered = JSON.stringify(tree.toJSON());
    expect(rendered).toContain('Etwas ist schiefgelaufen');
    expect(rendered).toContain('BOOM');
    expect(rendered).toContain('Zurueck zum Start');
    expect(onError).toHaveBeenCalled();
    tree.unmount();
    errSpy.mockRestore();
  });

  test('Reset-Handler leert den Fehler-State und zeigt wieder Children', () => {
    const errSpy = jest.spyOn(console, 'error').mockImplementation((): void => undefined);
    let raise = true;
    function MaybeBoom(): React.JSX.Element {
      if (raise) throw new Error('BOOM');
      return <Text>ok</Text>;
    }
    const tree = TestRenderer.create(
      <ErrorBoundary>
        <MaybeBoom />
      </ErrorBoundary>,
    );
    let rendered = JSON.stringify(tree.toJSON());
    expect(rendered).toContain('Etwas ist schiefgelaufen');

    // Fallback-Button anklicken. react-test-renderer findet ihn ueber props.
    // Alle Elemente mit onPress-Handler finden (Pressable landet als host mit
    // Type-String 'Pressable' im Baum).
    const pressables = tree.root.findAll(
      (n) => typeof (n.props as { onPress?: unknown }).onPress === 'function',
    );
    expect(pressables.length).toBeGreaterThan(0);
    raise = false;
    act(() => {
      pressables[0].props.onPress();
    });
    rendered = JSON.stringify(tree.toJSON());
    expect(rendered).toContain('ok');
    tree.unmount();
    errSpy.mockRestore();
  });
});
