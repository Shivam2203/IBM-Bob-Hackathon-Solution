# Setup Instructions

Complete setup guide for the Calculator project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for version control)

## Installation Steps

### 1. Install the Package

```bash
# Install in editable mode (for development)
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### 2. Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

This installs:
- pytest (testing framework)
- pytest-cov (coverage reporting)
- black (code formatter)
- flake8 (linter)
- mypy (type checker)
- pre-commit (git hooks)

### 3. Setup Pre-commit Hooks

```bash
pre-commit install
```

This will automatically run code quality checks before each commit.

## Verification

### Test the Installation

```bash
# Test import
python -c "from calculator import add, subtract, multiply, divide, power, factorial; print('Import successful!')"

# Run a simple calculation
python -c "from calculator import add; print(f'2 + 3 = {add(2, 3)}')"
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/calculator --cov-report=html

# Open coverage report
# Windows: start htmlcov/index.html
# macOS: open htmlcov/index.html
# Linux: xdg-open htmlcov/index.html
```

### Check Code Quality

```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/

# Run all pre-commit hooks
pre-commit run --all-files
```

## Common Issues

### Issue: Import Error

**Problem**: `ModuleNotFoundError: No module named 'calculator'`

**Solution**: Install the package in editable mode:
```bash
pip install -e .
```

### Issue: pytest not found

**Problem**: `pytest: command not found`

**Solution**: Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

### Issue: Pre-commit hooks failing

**Problem**: Pre-commit hooks fail on first run

**Solution**: This is normal. Fix the issues reported and commit again:
```bash
# Fix formatting
black src/ tests/

# Fix linting issues
flake8 src/ tests/

# Commit again
git commit -m "your message"
```

## Next Steps

1. Read the [README.md](README.md) for project overview
2. Check [docs/API.md](docs/API.md) for API reference
3. See [docs/USAGE.md](docs/USAGE.md) for usage examples
4. Review [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for contribution guidelines

## Quick Start Example

```python
from calculator import add, subtract, multiply, divide, power, factorial

# Basic operations
print(add(5, 3))        # 8
print(subtract(10, 4))  # 6
print(multiply(7, 6))   # 42
print(divide(15, 3))    # 5.0

# Advanced operations
print(power(2, 10))     # 1024
print(factorial(5))     # 120

# Error handling
result = divide(10, 0)
if isinstance(result, str):
    print(f"Error: {result}")
else:
    print(f"Result: {result}")
```

## Development Workflow

1. Create a branch: `git checkout -b feature/your-feature`
2. Make changes
3. Run tests: `pytest`
4. Check quality: `pre-commit run --all-files`
5. Commit: `git commit -m "feat: your feature"`
6. Push: `git push origin feature/your-feature`
7. Create Pull Request

## Support

For issues or questions:
- Check existing issues on GitHub
- Read the documentation in `docs/`
- Contact the maintainers