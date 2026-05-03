# Project Advanced Coding Rules (Non-Obvious Only)

## Error Handling Pattern
- Functions return error **strings** (not exceptions) for error cases
- Error messages must start with "Error: " prefix
- Always check `isinstance(result, str)` before using divide() or factorial() results

## Implementation Constraints
- `power()` MUST use iterative multiplication (not `**` operator or recursion)
- `factorial()` MUST use iterative loop (not recursive implementation)
- All functions MUST be stateless - no global state or side effects

## Type System
- `divide()` returns `Union[float, str]` - handle both types
- `factorial()` returns `Union[int, str]` - handle both types
- All other functions return numeric types only (float or int)

## Package Structure
- Source code in `src/calculator/` (not root directory)
- Import as: `from calculator import add` (not `from src.calculator import add`)
- `py.typed` marker file required for PEP 561 compliance

## Code Quality Requirements
- Black formatting: 88 character line length (not 79)
- Flake8 ignores: E203, W503 (Black compatibility)
- MyPy strict mode for src/ (relaxed for tests/)
- All functions require complete type hints and Google-style docstrings

## Testing
- Tests in `tests/` directory (not alongside source)
- Use parametrized tests: `@pytest.mark.parametrize`
- Run single test: `pytest tests/test_calculator.py::TestAddition::test_add_various_inputs`

## Access To
- MCP tools available
- Browser tools available