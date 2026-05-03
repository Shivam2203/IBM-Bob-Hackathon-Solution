# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Project-Specific Rules (Non-Obvious Only)

### Error Handling Pattern
- Functions return error **strings** (not exceptions) for error cases
- Error messages must start with "Error: " prefix
- Check return type with `isinstance(result, str)` before using result

### Implementation Approach
- `power()` uses **iterative** multiplication (not `**` operator or recursion)
- `factorial()` uses **iterative** loop (not recursive implementation)
- All functions are **stateless** - no global state or side effects

### Type Annotations
- `divide()` returns `Union[float, str]` (not just float)
- `factorial()` returns `Union[int, str]` (not just int)
- All other functions return numeric types only

### Testing
- Test files must be in `tests/` directory for pytest discovery
- Use parametrized tests for multiple input combinations
- Coverage reports generated in `htmlcov/` directory
- Run single test: `pytest tests/test_calculator.py::TestAddition::test_add_various_inputs`

### Code Quality
- Black formatting: 88 character line length (not 79)
- Flake8 ignores: E203, W503 (Black compatibility)
- MyPy strict mode enabled for src/ (relaxed for tests/)
- Pre-commit hooks enforce all quality checks before commit

### Package Structure
- Source code in `src/calculator/` (not root directory)
- `py.typed` marker file required for PEP 561 type hint distribution
- Package imports: `from calculator import add` (not `from src.calculator import add`)