# BAAS Testing Hierarchy

## 1. Top-Level Tests (`/tests/`)
- `e2e/`: Full system scenarios (e.g., Book creation to completed Draft).
- `rag_eval/`: Retrieval and generation quality evaluation (Ragas, precision/recall).
- `agents_eval/`: Agentic workflow behavior and safety evaluation.

## 2. App-Specific Tests (`/apps/*/tests/`)
- `unit/`: Business logic, dependency-free.
- `integration/`: API endpoints, DB, and DI (with mocks/containers).
- `contract/`: OpenAPI schema consistency.

## 3. Package Tests (`/packages/*/tests/`)
- `unit/`: Pure function and domain model validation.
- `nodes/`: LangGraph node-level logic (isolated).
- `graphs/`: LangGraph routing and state invariant checks.
- `golden/`: LLM output snapshot/regression testing.
