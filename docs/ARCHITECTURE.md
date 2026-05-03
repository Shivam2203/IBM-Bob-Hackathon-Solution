# Architecture Documentation

System design and architecture overview for the Calculator package.

## Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Component Design](#component-design)
- [Data Flow](#data-flow)
- [Design Decisions](#design-decisions)
- [Error Handling Strategy](#error-handling-strategy)
- [Testing Architecture](#testing-architecture)
- [Future Enhancements](#future-enhancements)

---

## Overview

The Calculator package is a lightweight, pure-Python library providing basic and advanced mathematical operations with a focus on:

- **Simplicity**: Minimal dependencies (Python standard library only)
- **Type Safety**: Complete type hints for all functions
- **Reliability**: Comprehensive test coverage (100%)
- **Maintainability**: Clean code with extensive documentation

### Key Characteristics

- **Stateless Functions**: All operations are pure functions with no side effects
- **Iterative Implementations**: Power and factorial use loops instead of recursion
- **Error Handling**: Returns error strings instead of raising exceptions
- **Type Annotations**: Full typing support for IDE integration

---

## System Architecture

### High-Level Architecture

```mermaid
graph TB
    User[User Application] --> API[Calculator API]
    API --> Add[add function]
    API --> Sub[subtract function]
    API --> Mul[multiply function]
    API --> Div[divide function]
    API --> Pow[power function]
    API --> Fact[factorial function]
    
    Div --> ErrCheck1{b == 0?}
    ErrCheck1 -->|Yes| Err1[Return Error String]
    ErrCheck1 -->|No| Calc1[Calculate Result]
    
    Fact --> ErrCheck2{n < 0?}
    ErrCheck2 -->|Yes| Err2[Return Error String]
    ErrCheck2 -->|No| Calc2[Calculate Result]
    
    style API fill:#e1f5ff
    style Err1 fill:#ffebee
    style Err2 fill:#ffebee
```

### Package Structure

```mermaid
graph LR
    Root[calculator/] --> Src[src/]
    Root --> Tests[tests/]
    Root --> Docs[docs/]
    Root --> Config[Configuration Files]
    
    Src --> CalcPkg[calculator/]
    CalcPkg --> Init[__init__.py]
    CalcPkg --> Calc[calculator.py]
    CalcPkg --> Typed[py.typed]
    
    Tests --> TestInit[__init__.py]
    Tests --> Conf[conftest.py]
    Tests --> TestCalc[test_calculator.py]
    Tests --> TestEdge[test_edge_cases.py]
    
    Docs --> API[API.md]
    Docs --> Usage[USAGE.md]
    Docs --> Arch[ARCHITECTURE.md]
    Docs --> Contrib[CONTRIBUTING.md]
    
    Config --> Pyproject[pyproject.toml]
    Config --> Setup[setup.py]
    Config --> Flake[.flake8]
    Config --> Mypy[mypy.ini]
    
    style CalcPkg fill:#c8e6c9
    style Tests fill:#fff9c4
    style Docs fill:#e1bee7
    style Config fill:#b3e5fc
```

---

## Component Design

### Core Functions

#### Basic Arithmetic Operations

```mermaid
graph TD
    A[Basic Operations] --> B[add a, b]
    A --> C[subtract a, b]
    A --> D[multiply a, b]
    A --> E[divide a, b]
    
    B --> B1[return a + b]
    C --> C1[return a - b]
    D --> D1[return a * b]
    E --> E1{b == 0?}
    E1 -->|Yes| E2[return Error String]
    E1 -->|No| E3[return a / b]
    
    style A fill:#4caf50
    style E2 fill:#f44336
```

#### Advanced Operations

```mermaid
graph TD
    A[Advanced Operations] --> B[power base, exp]
    A --> C[factorial n]
    
    B --> B1[result = 1]
    B1 --> B2[Loop exp times]
    B2 --> B3[result *= base]
    B3 --> B4[return result]
    
    C --> C1{n < 0?}
    C1 -->|Yes| C2[return Error String]
    C1 -->|No| C3{n == 0 or 1?}
    C3 -->|Yes| C4[return 1]
    C3 -->|No| C5[Loop 2 to n]
    C5 --> C6[result *= i]
    C6 --> C7[return result]
    
    style A fill:#2196f3
    style C2 fill:#f44336
```

### Function Signatures

```python
# Type signatures for all functions
def add(a: float, b: float) -> float
def subtract(a: float, b: float) -> float
def multiply(a: float, b: float) -> float
def divide(a: float, b: float) -> Union[float, str]
def power(base: float, exponent: int) -> float
def factorial(n: int) -> Union[int, str]
```

---

## Data Flow

### Successful Operation Flow

```mermaid
sequenceDiagram
    participant User
    participant Calculator
    participant Function
    
    User->>Calculator: Import function
    User->>Function: Call with valid inputs
    Function->>Function: Validate inputs
    Function->>Function: Perform calculation
    Function->>User: Return numeric result
```

### Error Handling Flow

```mermaid
sequenceDiagram
    participant User
    participant Calculator
    participant Function
    
    User->>Calculator: Import function
    User->>Function: Call with invalid inputs
    Function->>Function: Detect error condition
    Function->>Function: Generate error message
    Function->>User: Return error string
    User->>User: Check isinstance(result, str)
    User->>User: Handle error appropriately
```

### Calculation Pipeline Example

```mermaid
graph LR
    A[Input: 10, 5] --> B[add 10, 5]
    B --> C[Result: 15]
    C --> D[multiply 15, 2]
    D --> E[Result: 30]
    E --> F[divide 30, 3]
    F --> G[Result: 10.0]
    
    style A fill:#e3f2fd
    style G fill:#c8e6c9
```

---

## Design Decisions

### 1. Error Handling: Strings vs Exceptions

**Decision**: Return error strings instead of raising exceptions

**Rationale**:
- Simpler for basic use cases
- Explicit error checking required
- No try-catch overhead for users
- Clear error messages

**Trade-offs**:
- Users must check return types
- Less Pythonic than exceptions
- Can't use standard exception handling patterns

**Example**:
```python
# Current approach
result = divide(10, 0)
if isinstance(result, str):
    print(f"Error: {result}")

# Alternative (not used)
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

### 2. Iterative vs Recursive Implementation

**Decision**: Use iterative implementations for power and factorial

**Rationale**:
- Avoids stack overflow for large inputs
- More predictable performance
- Easier to understand for beginners
- No recursion depth limits

**Trade-offs**:
- Slightly more verbose code
- Less elegant than recursive solutions

**Example**:
```python
# Iterative (used)
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive (not used)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### 3. Type Hints: Union Types for Errors

**Decision**: Use `Union[float, str]` and `Union[int, str]` for error-prone functions

**Rationale**:
- Explicit about possible return types
- IDE support for type checking
- Clear documentation of behavior
- MyPy compatibility

**Example**:
```python
from typing import Union

def divide(a: float, b: float) -> Union[float, str]:
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

### 4. Pure Functions (No State)

**Decision**: All functions are stateless and pure

**Rationale**:
- Predictable behavior
- Easy to test
- Thread-safe by design
- No hidden dependencies

**Characteristics**:
- Same inputs always produce same outputs
- No side effects
- No global state modification
- No I/O operations

---

## Error Handling Strategy

### Error Categories

```mermaid
graph TD
    A[Error Types] --> B[Mathematical Errors]
    A --> C[Input Validation Errors]
    
    B --> B1[Division by Zero]
    B --> B2[Negative Factorial]
    
    C --> C1[Type Errors - Handled by Python]
    C --> C2[Value Errors - Handled by Functions]
    
    style B1 fill:#ffcdd2
    style B2 fill:#ffcdd2
```

### Error Messages

All error messages follow a consistent format:

```
"Error: <Description of the problem>"
```

Examples:
- `"Error: Division by zero"`
- `"Error: Factorial not defined for negative numbers"`

### Error Detection Pattern

```python
# Pattern used in divide function
def divide(a: float, b: float) -> Union[float, str]:
    if b == 0:  # Error condition check
        return "Error: Division by zero"  # Error message
    return a / b  # Normal calculation

# Pattern used in factorial function
def factorial(n: int) -> Union[int, str]:
    if n < 0:  # Error condition check
        return "Error: Factorial not defined for negative numbers"
    # ... normal calculation
```

---

## Testing Architecture

### Test Organization

```mermaid
graph TD
    A[Test Suite] --> B[Unit Tests]
    A --> C[Edge Case Tests]
    A --> D[Integration Tests]
    
    B --> B1[test_calculator.py]
    B1 --> B2[TestAddition]
    B1 --> B3[TestSubtraction]
    B1 --> B4[TestMultiplication]
    B1 --> B5[TestDivision]
    B1 --> B6[TestPower]
    B1 --> B7[TestFactorial]
    
    C --> C1[test_edge_cases.py]
    C1 --> C2[TestDivisionEdgeCases]
    C1 --> C3[TestFactorialEdgeCases]
    C1 --> C4[TestPowerEdgeCases]
    C1 --> C5[TestTypeConsistency]
    
    D --> D1[conftest.py]
    D1 --> D2[Fixtures]
    D1 --> D3[Test Configuration]
    
    style A fill:#4caf50
    style B fill:#2196f3
    style C fill:#ff9800
    style D fill:#9c27b0
```

### Test Coverage Strategy

```mermaid
graph LR
    A[Test Coverage] --> B[Normal Cases]
    A --> C[Edge Cases]
    A --> D[Error Cases]
    A --> E[Type Checking]
    
    B --> B1[Positive Numbers]
    B --> B2[Negative Numbers]
    B --> B3[Zero]
    B --> B4[Decimals]
    
    C --> C1[Large Numbers]
    C --> C2[Boundary Values]
    C --> C3[Precision]
    
    D --> D1[Division by Zero]
    D --> D2[Negative Factorial]
    
    E --> E1[Return Types]
    E --> E2[Type Consistency]
    
    style A fill:#4caf50
```

### Parametrized Testing

Tests use pytest's parametrize decorator for efficiency:

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_add_various_inputs(a, b, expected):
    assert add(a, b) == expected
```

---

## Future Enhancements

### Potential Improvements

1. **Additional Operations**
   - Square root
   - Logarithms
   - Trigonometric functions
   - Statistical functions (mean, median, mode)

2. **Performance Optimizations**
   - Memoization for factorial
   - Fast exponentiation algorithm for power
   - Caching for repeated calculations

3. **Enhanced Error Handling**
   - Custom exception classes
   - More detailed error messages
   - Error codes for programmatic handling

4. **Extended Functionality**
   - Complex number support
   - Matrix operations
   - Vector calculations
   - Symbolic mathematics

5. **API Improvements**
   - Calculator class with state
   - Calculation history
   - Undo/redo functionality
   - Expression parsing

### Extensibility Points

```mermaid
graph TD
    A[Extension Points] --> B[New Operations]
    A --> C[Error Handling]
    A --> D[Type System]
    A --> E[Performance]
    
    B --> B1[Add new functions]
    B --> B2[Maintain consistency]
    
    C --> C1[Custom exceptions]
    C --> C2[Error recovery]
    
    D --> D1[Generic types]
    D --> D2[Protocol support]
    
    E --> E1[Caching layer]
    E --> E2[Optimization]
    
    style A fill:#9c27b0
```

---

## Performance Characteristics

### Time Complexity

| Function | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| add | O(1) | O(1) |
| subtract | O(1) | O(1) |
| multiply | O(1) | O(1) |
| divide | O(1) | O(1) |
| power | O(n) where n = exponent | O(1) |
| factorial | O(n) where n = input | O(1) |

### Scalability Considerations

```mermaid
graph LR
    A[Input Size] --> B{Operation Type}
    B -->|Basic Arithmetic| C[Constant Time]
    B -->|Power| D[Linear in Exponent]
    B -->|Factorial| E[Linear in Input]
    
    C --> F[Scales Well]
    D --> G[Good for Small Exponents]
    E --> H[Limited by Integer Size]
    
    style C fill:#4caf50
    style D fill:#ff9800
    style E fill:#f44336
```

---

## Conclusion

The Calculator package demonstrates a clean, well-tested architecture with:

- Clear separation of concerns
- Comprehensive error handling
- Full type safety
- Extensive documentation
- 100% test coverage

The design prioritizes simplicity, reliability, and maintainability while providing a solid foundation for future enhancements.

---

## Related Documentation

- [API Reference](API.md) - Complete function documentation
- [Usage Guide](USAGE.md) - Usage examples and patterns
- [Contributing](CONTRIBUTING.md) - Development guidelines