/** @type {import('jest').Config} */
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  // .tsx erlaubt Component-Tests (react-test-renderer).
  testMatch: [
    '<rootDir>/src/**/__tests__/**/*.test.ts',
    '<rootDir>/src/**/__tests__/**/*.test.tsx',
  ],
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json'],
  // Native-Module werden gemockt. Tests unter Node duerfen sie NICHT wirklich laden.
  moduleNameMapper: {
    '^expo-sqlite$': '<rootDir>/src/db/__mocks__/expo-sqlite.ts',
    '^expo-location$': '<rootDir>/src/location/__mocks__/expo-location.ts',
    '^react-native$': '<rootDir>/src/__mocks__/react-native.tsx',
  },
};
