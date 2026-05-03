# Calculator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A professional Python calculator library with comprehensive testing, documentation, and quality assurance tools.

## Features

- ✨ **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division
- 🔢 **Advanced Functions**: Power (exponentiation) and factorial calculations
- 🛡️ **Error Handling**: Graceful handling of edge cases (division by zero, negative factorials)
- 📝 **Type Hints**: Full type annotations for better IDE support and type safety
- ✅ **100% Test Coverage**: Comprehensive test suite with pytest
- 📚 **Complete Documentation**: Detailed API reference and usage examples
- 🎨 **Code Quality**: Black formatting, Flake8 linting, MyPy type checking
- 🔄 **CI/CD**: Automated testing with GitHub Actions

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/Shivam2203/IBM-Bob-Hackathon-Solution.git
cd calculator

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Requirements

- Python 3.8 or higher
- No external runtime dependencies (uses Python standard library only)

## Quick Start

```python
from calculator import add, subtract, multiply, divide, power, factorial

# Basic arithmetic
result = add(5, 3)          # 8
result = subtract(10, 4)    # 6
result = multiply(7, 6)     # 42
result = divide(15, 3)      # 5.0

# Advanced operations
result = power(2, 10)       # 1024
result = factorial(5)       # 120

# Error handling
result = divide(10, 0)      # "Error: Division by zero"
result = factorial(-5)      # "Error: Factorial not defined for negative numbers"
```

## Documentation

- **[API Reference](docs/API.md)** - Complete function documentation
- **[Usage Guide](docs/USAGE.md)** - Detailed usage examples and patterns
- **[Architecture](docs/ARCHITECTURE.md)** - System design and architecture diagrams
- **[Contributing](docs/CONTRIBUTING.md)** - Guidelines for contributors

## Development

### Setup Development Environment

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src/calculator --cov-report=html

# Run specific test file
pytest tests/test_calculator.py

# Run specific test class
pytest tests/test_calculator.py::TestAddition

# Run specific test
pytest tests/test_calculator.py::TestAddition::test_add_various_inputs
```

### Code Quality

```bash
# Format code with Black
black src/ tests/

# Lint with Flake8
flake8 src/ tests/

# Type check with MyPy
mypy src/

# Run all pre-commit hooks
pre-commit run --all-files
```

## Project Structure

```
calculator/
├── src/
│   └── calculator/
│       ├── __init__.py          # Package initialization
│       ├── calculator.py        # Core calculator functions
│       └── py.typed             # PEP 561 type marker
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures
│   ├── test_calculator.py       # Unit tests
│   └── test_edge_cases.py       # Edge case tests
├── docs/
│   ├── API.md                   # API documentation
│   ├── USAGE.md                 # Usage examples
│   ├── ARCHITECTURE.md          # Architecture diagrams
│   └── CONTRIBUTING.md          # Contribution guidelines
├── .github/
│   └── workflows/
│       └── ci.yml               # CI/CD pipeline
├── pyproject.toml               # Project configuration
├── setup.py                     # Package setup
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies
├── .flake8                      # Flake8 configuration
├── mypy.ini                     # MyPy configuration
├── .gitignore                   # Git ignore patterns
├── .pre-commit-config.yaml      # Pre-commit hooks
└── README.md                    # This file
```

## API Overview

### Functions

- **`add(a: float, b: float) -> float`** - Add two numbers
- **`subtract(a: float, b: float) -> float`** - Subtract b from a
- **`multiply(a: float, b: float) -> float`** - Multiply two numbers
- **`divide(a: float, b: float) -> Union[float, str]`** - Divide a by b (returns error string if b is zero)
- **`power(base: float, exponent: int) -> float`** - Raise base to exponent power
- **`factorial(n: int) -> Union[int, str]`** - Calculate factorial of n (returns error string if n is negative)

See [API.md](docs/API.md) for detailed documentation.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](docs/CONTRIBUTING.md) for details on:

- Code of conduct
- Development setup
- Coding standards
- Testing requirements
- Pull request process

## Testing

This project maintains 100% test coverage with comprehensive test suites:

- **Unit Tests**: Test individual functions with various inputs
- **Edge Case Tests**: Test boundary conditions and error handling
- **Parametrized Tests**: Efficient testing of multiple input combinations
- **Type Tests**: Verify return type consistency

Run tests with: `pytest --cov=src/calculator`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- Shivam Patel - Initial work

## Acknowledgments

- Built with Python 3.8+
- Testing with pytest
- Code quality with Black, Flake8, and MyPy
- CI/CD with GitHub Actions

## Support

For issues, questions, or contributions, please visit:
- **Issues**: https://github.com/Shivam2203/IBM-Bob-Hackathon-Solution/issues
- **Discussions**: https://github.com/Shivam2203/IBM-Bob-Hackathon-Solution/discussions

---

Made with [Bob](image.png)! by the Shivam