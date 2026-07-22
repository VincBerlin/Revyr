// mobile/src/__mocks__/react-native.tsx
//
// Minimaler React-Native-Mock fuer Component-Tests unter Node + ts-jest.
// Rendert alle RN-Primitiven als React-Elemente mit Type-String ('View',
// 'Text', ...). react-test-renderer produziert daraus einen JSON-Baum, ohne
// den echten React-Native-Nativen-Modul-Layer zu laden.
//
// Aufloesung ueber moduleNameMapper in jest.config.js.

import React from 'react';

type AnyProps = Record<string, unknown> & { children?: React.ReactNode };

function makePassthrough(name: string): React.FC<AnyProps> {
  const Comp: React.FC<AnyProps> = (props) =>
    React.createElement(name, props, props.children);
  Comp.displayName = name;
  return Comp;
}

export const View = makePassthrough('View');
export const Text = makePassthrough('Text');
export const Pressable = makePassthrough('Pressable');
export const ScrollView = makePassthrough('ScrollView');
export const Switch = makePassthrough('Switch');
export const Button = makePassthrough('Button');
export const StatusBar = makePassthrough('StatusBar');

export const StyleSheet = {
  create<T extends Record<string, unknown>>(styles: T): T {
    return styles;
  },
  flatten: (style: unknown): unknown => style,
  compose: (a: unknown, b: unknown): unknown[] => [a, b],
  absoluteFill: {},
  hairlineWidth: 1,
};

export const Platform = {
  OS: 'ios' as const,
  select: <T,>(spec: { ios?: T; android?: T; default?: T }): T | undefined =>
    spec.ios ?? spec.default,
  Version: '18.0',
};

export type AppStateStatus = 'active' | 'background' | 'inactive';

export const AppState = {
  currentState: 'active' as AppStateStatus,
  addEventListener: (
    _type: string,
    _listener: (state: AppStateStatus) => void,
  ): { remove: () => void } => ({ remove: (): void => undefined }),
};

// Weitere gelegentlich importierte Symbole (defensiv):
export const Dimensions = {
  get: (): { width: number; height: number; scale: number; fontScale: number } => ({
    width: 400, height: 800, scale: 2, fontScale: 1,
  }),
  addEventListener: (): { remove: () => void } => ({ remove: (): void => undefined }),
};
