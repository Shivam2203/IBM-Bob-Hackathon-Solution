# Project Architecture Rules (Non-Obvious Only)

## Design Decisions
- Error handling via return strings (not exceptions) - intentional design choice
- Iterative implementations (not recursive) to avoid stack overflow
- Stateless pure functions (no class-based design) - architectural constraint
- Union return types for error-prone functions (divide, factorial)

## Package Architecture
- Source in `src/calculator/` but imports work as `from calculator import add`
- This is achieved through setup.py package_dir configuration
- `py.typed` marker required for PEP 561 type distribution

## Testing Strategy
- 100% coverage target (not just 80% or 90%)
- Separate files for unit tests and edge cases (organizational decision)
- Parametrized tests preferred over individual test functions
- Tests must be in `tests/` directory (not alongside source)

## Code Quality Pipeline
- Pre-commit hooks enforce quality before commit (not just in CI)
- Black with 88 char line length (not PEP 8's 79)
- MyPy strict mode for src/, relaxed for tests/ (intentional difference)
- Flake8 ignores E203, W503 for Black compatibility

## Performance Characteristics
- power() is O(n) in exponent (iterative, not O(log n) fast exponentiation)
- factorial() is O(n) (iterative, not memoized)
- All basic operations are O(1)
- No caching or optimization layers (intentional simplicity)

## Future Extensibility
- Pure function design allows easy addition of new operations
- No state means thread-safe by default
- Type hints enable static analysis and IDE support
- Modular structure supports plugin architecture if needed