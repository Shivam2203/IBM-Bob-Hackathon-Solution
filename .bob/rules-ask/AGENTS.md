# Project Documentation Rules (Non-Obvious Only)

## Documentation Structure
- Main docs in `docs/` directory (API.md, USAGE.md, ARCHITECTURE.md, CONTRIBUTING.md)
- Root README.md is project overview, not detailed documentation
- API reference uses Google-style docstring format
- Architecture diagrams use Mermaid syntax

## Code Organization
- Source in `src/calculator/` (not root or just `calculator/`)
- Tests in `tests/` (separate from source, not alongside)
- Package imports work as `from calculator import add` despite src/ structure

## Error Handling Documentation
- Functions that return Union types (divide, factorial) need special documentation
- Error messages always start with "Error: " prefix
- Type checking pattern: `isinstance(result, str)` to detect errors

## Testing Documentation
- Test organization: Unit tests in test_calculator.py, edge cases in test_edge_cases.py
- Parametrized tests used extensively for efficiency
- Coverage reports in htmlcov/ directory (not in docs/)
- Single test run syntax documented: `pytest path::Class::test_method`

## Non-Standard Patterns
- Error handling via return strings (not exceptions) - counterintuitive for Python
- Iterative implementations (not recursive) for power and factorial
- Stateless functions only (no class-based calculator)