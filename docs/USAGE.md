# Usage Guide

Comprehensive usage examples and patterns for the Calculator package.

## Table of Contents

- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Advanced Usage](#advanced-usage)
- [Error Handling](#error-handling)
- [Common Patterns](#common-patterns)
- [Integration Examples](#integration-examples)
- [Best Practices](#best-practices)
- [Performance Considerations](#performance-considerations)

---

## Installation

### Standard Installation

```bash
pip install calculator
```

### Development Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/calculator.git
cd calculator

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```

---

## Basic Usage

### Simple Arithmetic Operations

```python
from calculator import add, subtract, multiply, divide

# Addition
total = add(10, 5)
print(f"10 + 5 = {total}")  # Output: 10 + 5 = 15

# Subtraction
difference = subtract(10, 5)
print(f"10 - 5 = {difference}")  # Output: 10 - 5 = 5

# Multiplication
product = multiply(10, 5)
print(f"10 × 5 = {product}")  # Output: 10 × 5 = 50

# Division
quotient = divide(10, 5)
print(f"10 ÷ 5 = {quotient}")  # Output: 10 ÷ 5 = 2.0
```

### Advanced Operations

```python
from calculator import power, factorial

# Exponentiation
result = power(2, 8)
print(f"2^8 = {result}")  # Output: 2^8 = 256

# Factorial
result = factorial(6)
print(f"6! = {result}")  # Output: 6! = 720
```

---

## Advanced Usage

### Chaining Operations

```python
from calculator import add, multiply, divide

# Calculate: (10 + 5) × 3 ÷ 2
step1 = add(10, 5)        # 15
step2 = multiply(step1, 3)  # 45
result = divide(step2, 2)   # 22.5

print(f"Result: {result}")  # Output: Result: 22.5
```

### Working with Lists

```python
from calculator import add, multiply
from functools import reduce

# Sum a list of numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(f"Sum: {total}")  # Output: Sum: 15

# Product of a list
numbers = [2, 3, 4]
product = reduce(multiply, numbers)
print(f"Product: {product}")  # Output: Product: 24
```

### Complex Calculations

```python
from calculator import add, subtract, multiply, divide, power

def calculate_compound_interest(principal, rate, time):
    """Calculate compound interest using calculator functions."""
    # Formula: A = P(1 + r)^t
    rate_plus_one = add(1, rate)
    power_result = power(rate_plus_one, time)
    amount = multiply(principal, power_result)
    interest = subtract(amount, principal)
    return interest

# Calculate interest on $1000 at 5% for 10 years
interest = calculate_compound_interest(1000, 0.05, 10)
print(f"Interest: ${interest:.2f}")
```

---

## Error Handling

### Division by Zero

```python
from calculator import divide

def safe_divide(a, b):
    """Safely divide two numbers with error handling."""
    result = divide(a, b)
    
    if isinstance(result, str):
        print(f"Error: Cannot divide {a} by {b}")
        return None
    
    return result

# Usage
result = safe_divide(10, 2)
print(f"10 ÷ 2 = {result}")  # Output: 10 ÷ 2 = 5.0

result = safe_divide(10, 0)
# Output: Error: Cannot divide 10 by 0
print(f"Result: {result}")  # Output: Result: None
```

### Negative Factorial

```python
from calculator import factorial

def safe_factorial(n):
    """Safely calculate factorial with error handling."""
    if n < 0:
        raise ValueError(f"Factorial not defined for negative numbers: {n}")
    
    result = factorial(n)
    
    if isinstance(result, str):
        raise ValueError(result)
    
    return result

# Usage
try:
    result = safe_factorial(5)
    print(f"5! = {result}")  # Output: 5! = 120
    
    result = safe_factorial(-5)
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Factorial not defined for negative numbers: -5
```

### Comprehensive Error Handler

```python
from calculator import divide, factorial
from typing import Union

def handle_calculator_result(result: Union[int, float, str], operation: str) -> Union[int, float]:
    """Handle calculator results with error checking."""
    if isinstance(result, str):
        raise RuntimeError(f"{operation} failed: {result}")
    return result

# Usage
try:
    result = divide(10, 0)
    result = handle_calculator_result(result, "Division")
except RuntimeError as e:
    print(f"Error: {e}")
    # Output: Error: Division failed: Error: Division by zero
```

---

## Common Patterns

### Calculator Class Wrapper

```python
from calculator import add, subtract, multiply, divide, power, factorial

class Calculator:
    """Object-oriented wrapper for calculator functions."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = subtract(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = multiply(a, b)
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        result = divide(a, b)
        if isinstance(result, str):
            self.history.append(f"{a} ÷ {b} = ERROR")
            raise ValueError(result)
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def get_history(self):
        return self.history

# Usage
calc = Calculator()
calc.add(5, 3)
calc.multiply(4, 2)
calc.subtract(10, 3)

print("Calculation History:")
for entry in calc.get_history():
    print(f"  {entry}")
```

### Statistical Calculations

```python
from calculator import add, divide, power, subtract
from functools import reduce

def mean(numbers):
    """Calculate the mean of a list of numbers."""
    total = reduce(add, numbers)
    count = len(numbers)
    return divide(total, count)

def variance(numbers):
    """Calculate the variance of a list of numbers."""
    avg = mean(numbers)
    squared_diffs = [power(subtract(x, avg), 2) for x in numbers]
    return mean(squared_diffs)

# Usage
data = [2, 4, 6, 8, 10]
print(f"Mean: {mean(data)}")      # Output: Mean: 6.0
print(f"Variance: {variance(data)}")  # Output: Variance: 8.0
```

### Recursive Patterns

```python
from calculator import multiply, add

def fibonacci(n):
    """Calculate nth Fibonacci number using calculator functions."""
    if n <= 1:
        return n
    return add(fibonacci(subtract(n, 1)), fibonacci(subtract(n, 2)))

def sum_of_squares(n):
    """Calculate sum of squares from 1 to n."""
    if n == 0:
        return 0
    return add(power(n, 2), sum_of_squares(subtract(n, 1)))

# Usage
print(f"10th Fibonacci: {fibonacci(10)}")  # Output: 10th Fibonacci: 55
print(f"Sum of squares 1-5: {sum_of_squares(5)}")  # Output: Sum of squares 1-5: 55
```

---

## Integration Examples

### Command-Line Interface

```python
import sys
from calculator import add, subtract, multiply, divide, power, factorial

def cli_calculator():
    """Simple CLI calculator."""
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'power': power,
        'factorial': factorial
    }
    
    if len(sys.argv) < 2:
        print("Usage: python calculator_cli.py <operation> <args>")
        return
    
    operation = sys.argv[1]
    
    if operation not in operations:
        print(f"Unknown operation: {operation}")
        return
    
    if operation == 'factorial':
        n = int(sys.argv[2])
        result = factorial(n)
    else:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        result = operations[operation](a, b)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    cli_calculator()
```

### Web API Integration

```python
from flask import Flask, jsonify, request
from calculator import add, subtract, multiply, divide, power, factorial

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    """API endpoint for calculations."""
    data = request.json
    operation = data.get('operation')
    
    operations = {
        'add': lambda: add(data['a'], data['b']),
        'subtract': lambda: subtract(data['a'], data['b']),
        'multiply': lambda: multiply(data['a'], data['b']),
        'divide': lambda: divide(data['a'], data['b']),
        'power': lambda: power(data['base'], data['exponent']),
        'factorial': lambda: factorial(data['n'])
    }
    
    if operation not in operations:
        return jsonify({'error': 'Invalid operation'}), 400
    
    result = operations[operation]()
    
    if isinstance(result, str):
        return jsonify({'error': result}), 400
    
    return jsonify({'result': result})

# Run with: flask run
```

---

## Best Practices

### 1. Always Check Return Types for Error-Prone Functions

```python
from calculator import divide, factorial

# Good
result = divide(10, 2)
if isinstance(result, str):
    # Handle error
    print(f"Error: {result}")
else:
    # Use result
    print(f"Result: {result}")

# Bad - assumes success
result = divide(10, 0)
print(f"Result: {result * 2}")  # Will fail if result is a string
```

### 2. Use Type Hints in Your Code

```python
from calculator import add, multiply
from typing import List

def calculate_total(prices: List[float], tax_rate: float) -> float:
    """Calculate total with tax."""
    subtotal = sum(prices)  # Using built-in sum for efficiency
    tax = multiply(subtotal, tax_rate)
    return add(subtotal, tax)
```

### 3. Handle Edge Cases

```python
from calculator import divide, factorial

def safe_operations(a: float, b: float, n: int):
    """Demonstrate safe operation handling."""
    # Check for division by zero before calling
    if b == 0:
        print("Cannot divide by zero")
        return None
    
    # Check for negative factorial before calling
    if n < 0:
        print("Cannot calculate factorial of negative number")
        return None
    
    division_result = divide(a, b)
    factorial_result = factorial(n)
    
    return division_result, factorial_result
```

---

## Performance Considerations

### 1. Large Factorial Calculations

```python
from calculator import factorial
import time

# Factorial grows very quickly
start = time.time()
result = factorial(20)
end = time.time()

print(f"factorial(20) = {result}")
print(f"Time: {end - start:.6f} seconds")

# Note: factorial(100) would be extremely large
# Consider using math.factorial for very large values in production
```

### 2. Repeated Operations

```python
from calculator import multiply

# Inefficient - repeated function calls
def calculate_area_inefficient(width, height, count):
    areas = []
    for _ in range(count):
        areas.append(multiply(width, height))
    return areas

# Efficient - calculate once
def calculate_area_efficient(width, height, count):
    area = multiply(width, height)
    return [area] * count

# The efficient version is much faster for large counts
```

### 3. Choosing the Right Function

```python
from calculator import power

# For small exponents, power() is fine
result = power(2, 10)  # Fast

# For very large exponents, consider alternatives
# power(2, 1000) would be slow due to iterative implementation
# In production, use: 2 ** 1000 or math.pow(2, 1000)
```

---

## Troubleshooting

### Common Issues

**Issue**: Import errors
```python
# Wrong
from calculator import Calculator  # No such class

# Correct
from calculator import add, subtract, multiply, divide, power, factorial
```

**Issue**: Type errors with division/factorial
```python
# Wrong - not checking return type
result = divide(10, 0)
print(result + 5)  # TypeError if result is string

# Correct
result = divide(10, 0)
if isinstance(result, (int, float)):
    print(result + 5)
else:
    print(f"Error: {result}")
```

---

## Additional Resources

- [API Reference](API.md) - Complete function documentation
- [Architecture](ARCHITECTURE.md) - System design and diagrams
- [Contributing](CONTRIBUTING.md) - Development guidelines

---

For more examples and use cases, check the test suite in `tests/` directory.