// tests/frontend/conftest.js
import { configure } from '@testing-library/react';
import { vi } from 'vitest';
import { cleanup } from '@testing-library/react';

// Testing Library
configure({ testIdAttribute: 'data-test-id' });

// Mocks globales
vi.mock('axios', () => ({
  get: vi.fn(() => Promise.resolve({ data: [] })),
}));

// Fixtures
export const mockUser = { id: 1, name: 'Test User' };

// Limpieza
afterEach(() => {
  cleanup();
  vi.resetAllMocks();
});