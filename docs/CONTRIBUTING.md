# Contributing to Calculator

Thank you for your interest in contributing to the Calculator project! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Requirements](#testing-requirements)
- [Documentation](#documentation)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, background, or identity.

### Expected Behavior

- Be respectful and considerate
- Welcome newcomers and help them get started
- Accept constructive criticism gracefully
- Focus on what is best for the project
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling or insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of Python and testing

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/calculator.git
cd calculator
```

3. Add the upstream repository:

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/calculator.git
```

---

## Development Setup

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install package in editable mode with dev dependencies
pip install -e ".[dev]"

# Or install from requirements files
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 3. Install Pre-commit Hooks

```bash
pre-commit install
```

This will automatically run code quality checks before each commit.

### 4. Verify Setup

```bash
# Run tests
pytest

# Run linting
flake8 src/ tests/

# Run type checking
mypy src/

# Run formatting check
black --check src/ tests/
```

---

## Development Workflow

### 1. Create a Branch

```bash
# Update your local main branch
git checkout main
git pull upstream main

# Create a new branch for your feature/fix
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### Branch Naming Convention

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `test/` - Test additions or modifications
- `refactor/` - Code refactoring

### 2. Make Changes

- Write your code following the [Code Style Guidelines](#code-style-guidelines)
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass

### 3. Commit Changes

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "feat: add new feature description"
```

See [Commit Message Guidelines](#commit-message-guidelines) for details.

### 4. Push and Create Pull Request

```bash
# Push your branch to your fork
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

---

## Code Style Guidelines

### Python Style

We follow PEP 8 with some modifications enforced by Black.

#### Formatting

- **Line Length**: 88 characters (Black default)
- **Indentation**: 4 spaces
- **Quotes**: Double quotes for strings (Black default)
- **Imports**: Organized with isort (Black profile)

#### Type Hints

All functions must have complete type hints:

```python
from typing import Union

def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

def divide(a: float, b: float) -> Union[float, str]:
    """Divide a by b, return error string if b is zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

#### Docstrings

Use Google-style docstrings:

```python
def function_name(param1: type1, param2: type2) -> return_type:
    """Brief description of function.

    Longer description if needed, explaining the function's purpose,
    behavior, and any important details.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Examples:
        >>> function_name(value1, value2)
        expected_result
    """
    # Implementation
```

#### Naming Conventions

- **Functions**: `snake_case`
- **Variables**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Classes**: `PascalCase` (if added in future)
- **Private**: Prefix with `_` (if needed)

#### Import Organization

```python
# Standard library imports
import sys
from typing import Union

# Third-party imports
import pytest

# Local imports
from calculator import add, subtract
```

### Code Quality Tools

#### Black (Formatting)

```bash
# Format all code
black src/ tests/

# Check formatting without changes
black --check src/ tests/
```

#### Flake8 (Linting)

```bash
# Run linting
flake8 src/ tests/

# Configuration in .flake8
```

#### MyPy (Type Checking)

```bash
# Run type checking
mypy src/

# Configuration in mypy.ini
```

#### Pre-commit

```bash
# Run all hooks manually
pre-commit run --all-files

# Hooks run automatically on commit
```

---

## Testing Requirements

### Test Coverage

- **Minimum**: 95% code coverage
- **Target**: 100% code coverage
- All new features must include tests
- All bug fixes must include regression tests

### Writing Tests

#### Test Structure

```python
import pytest
from calculator import function_name

class TestFunctionName:
    """Test cases for function_name."""

    def test_basic_case(self):
        """Test basic functionality."""
        result = function_name(input1, input2)
        assert result == expected

    @pytest.mark.parametrize("input1,input2,expected", [
        (value1, value2, result1),
        (value3, value4, result2),
    ])
    def test_multiple_cases(self, input1, input2, expected):
        """Test multiple input combinations."""
        assert function_name(input1, input2) == expected
```

#### Test Categories

1. **Unit Tests** (`test_calculator.py`)
   - Test individual functions
   - Normal input cases
   - Parametrized tests for efficiency

2. **Edge Case Tests** (`test_edge_cases.py`)
   - Boundary conditions
   - Error cases
   - Type consistency
   - Large numbers
   - Precision issues

3. **Integration Tests** (if applicable)
   - Function combinations
   - Real-world scenarios

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/calculator --cov-report=html

# Run specific test file
pytest tests/test_calculator.py

# Run specific test class
pytest tests/test_calculator.py::TestAddition

# Run specific test
pytest tests/test_calculator.py::TestAddition::test_add_various_inputs

# Run with verbose output
pytest -v

# Run and stop at first failure
pytest -x
```

### Test Fixtures

Use fixtures in `conftest.py` for shared test data:

```python
import pytest

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {"key": "value"}
```

---

## Documentation

### Documentation Requirements

- All public functions must have docstrings
- Update API.md for new functions
- Update USAGE.md with examples
- Update README.md if needed
- Add architecture diagrams for major changes

### Documentation Style

- Clear and concise
- Include examples
- Explain edge cases
- Document error conditions

### Building Documentation

```bash
# Documentation is in Markdown format
# View in any Markdown viewer or on GitHub
```

---

## Commit Message Guidelines

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```bash
# Feature
git commit -m "feat: add square root function"

# Bug fix
git commit -m "fix: handle division by zero correctly"

# Documentation
git commit -m "docs: update API reference for new functions"

# Test
git commit -m "test: add edge cases for factorial function"
```

### Best Practices

- Use present tense ("add feature" not "added feature")
- Use imperative mood ("move cursor to..." not "moves cursor to...")
- Keep subject line under 50 characters
- Capitalize subject line
- Don't end subject line with period
- Separate subject from body with blank line
- Wrap body at 72 characters
- Explain what and why, not how

---

## Pull Request Process

### Before Submitting

1. ✅ All tests pass
2. ✅ Code coverage maintained or improved
3. ✅ Code follows style guidelines
4. ✅ Documentation updated
5. ✅ Commit messages follow guidelines
6. ✅ Branch is up to date with main

### PR Checklist

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Coverage maintained/improved

## Documentation
- [ ] Docstrings updated
- [ ] API.md updated
- [ ] USAGE.md updated
- [ ] README.md updated (if needed)

## Code Quality
- [ ] Black formatting applied
- [ ] Flake8 linting passed
- [ ] MyPy type checking passed
- [ ] Pre-commit hooks passed
```

### Review Process

1. Automated checks run (CI/CD)
2. Code review by maintainers
3. Address feedback
4. Approval and merge

### After Merge

1. Delete your branch
2. Update your local repository:

```bash
git checkout main
git pull upstream main
```

---

## Issue Reporting

### Bug Reports

Include:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: Detailed steps
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**: Python version, OS, etc.
- **Code Sample**: Minimal reproducible example

### Feature Requests

Include:

- **Description**: Clear description of feature
- **Use Case**: Why is this needed?
- **Proposed Solution**: How should it work?
- **Alternatives**: Other approaches considered

### Issue Template

```markdown
## Description
[Clear description]

## Steps to Reproduce (for bugs)
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- Python version:
- OS:
- Calculator version:

## Code Sample
```python
# Minimal reproducible example
```
```

---

## Questions?

- Check existing issues and pull requests
- Read the documentation
- Ask in discussions
- Contact maintainers

---

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to Calculator! 🎉