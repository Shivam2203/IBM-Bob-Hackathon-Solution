# API Reference

Complete API documentation for the Calculator package.

## Table of Contents

- [add](#add)
- [subtract](#subtract)
- [multiply](#multiply)
- [divide](#divide)
- [power](#power)
- [factorial](#factorial)

---

## add

```python
def add(a: float, b: float) -> float
```

Adds two numbers together.

### Parameters

- **a** (`float`): First number to add
- **b** (`float`): Second number to add

### Returns

- `float`: The sum of a and b

### Examples

```python
from calculator import add

# Basic addition
result = add(2, 3)
print(result)  # Output: 5

# Adding negative numbers
result = add(-1, 1)
print(result)  # Output: 0

# Adding decimals
result = add(1.5, 2.5)
print(result)  # Output: 4.0

# Adding large numbers
result = add(1000000, 2000000)
print(result)  # Output: 3000000
```

### Notes

- Addition is commutative: `add(a, b) == add(b, a)`
- Adding zero returns the original number: `add(x, 0) == x`
- Works with integers, floats, and negative numbers

---

## subtract

```python
def subtract(a: float, b: float) -> float
```

Subtracts the second number from the first.

### Parameters

- **a** (`float`): Number to subtract from (minuend)
- **b** (`float`): Number to subtract (subtrahend)

### Returns

- `float`: The difference of a and b (a - b)

### Examples

```python
from calculator import subtract

# Basic subtraction
result = subtract(5, 3)
print(result)  # Output: 2

# Subtracting larger from smaller
result = subtract(0, 5)
print(result)  # Output: -5

# Subtracting negative numbers
result = subtract(-3, -2)
print(result)  # Output: -1

# Subtracting decimals
result = subtract(10.5, 5.5)
print(result)  # Output: 5.0
```

### Notes

- Subtraction is NOT commutative: `subtract(a, b) != subtract(b, a)`
- Subtracting zero returns the original number: `subtract(x, 0) == x`
- Subtracting a number from itself returns zero: `subtract(x, x) == 0`

---

## multiply

```python
def multiply(a: float, b: float) -> float
```

Multiplies two numbers together.

### Parameters

- **a** (`float`): First number to multiply
- **b** (`float`): Second number to multiply

### Returns

- `float`: The product of a and b

### Examples

```python
from calculator import multiply

# Basic multiplication
result = multiply(3, 4)
print(result)  # Output: 12

# Multiplying by zero
result = multiply(0, 100)
print(result)  # Output: 0

# Multiplying negative numbers
result = multiply(-2, 5)
print(result)  # Output: -10

# Multiplying decimals
result = multiply(2.5, 4)
print(result)  # Output: 10.0
```

### Notes

- Multiplication is commutative: `multiply(a, b) == multiply(b, a)`
- Multiplying by zero always returns zero: `multiply(x, 0) == 0`
- Multiplying by one returns the original number: `multiply(x, 1) == x`
- Multiplying two negative numbers returns a positive result

---

## divide

```python
def divide(a: float, b: float) -> Union[float, str]
```

Divides the first number by the second.

### Parameters

- **a** (`float`): Numerator (number to be divided)
- **b** (`float`): Denominator (number to divide by)

### Returns

- `float`: The quotient of a and b (a / b)
- `str`: Error message if b is zero

### Error Handling

Returns the string `"Error: Division by zero"` when attempting to divide by zero.

### Examples

```python
from calculator import divide

# Basic division
result = divide(10, 2)
print(result)  # Output: 5.0

# Division with remainder
result = divide(7, 2)
print(result)  # Output: 3.5

# Division by zero (error case)
result = divide(10, 0)
print(result)  # Output: "Error: Division by zero"

# Dividing negative numbers
result = divide(-10, 2)
print(result)  # Output: -5.0

# Dividing zero
result = divide(0, 5)
print(result)  # Output: 0.0
```

### Notes

- Division is NOT commutative: `divide(a, b) != divide(b, a)`
- Dividing by one returns the original number: `divide(x, 1) == x`
- Dividing a number by itself returns 1: `divide(x, x) == 1.0` (when x != 0)
- Always returns a float (not an integer) for successful divisions
- Check return type to handle error cases: `isinstance(result, str)`

---

## power

```python
def power(base: float, exponent: int) -> float
```

Raises a base number to an exponent power using iterative calculation.

### Parameters

- **base** (`float`): The base number
- **exponent** (`int`): The exponent (must be non-negative integer)

### Returns

- `float`: The result of base raised to the power of exponent

### Implementation Note

This function uses an iterative approach (loop-based multiplication) rather than the built-in `**` operator.

### Examples

```python
from calculator import power

# Basic exponentiation
result = power(2, 3)
print(result)  # Output: 8

# Power of zero
result = power(5, 0)
print(result)  # Output: 1

# Large exponents
result = power(10, 2)
print(result)  # Output: 100

# Base of zero
result = power(0, 5)
print(result)  # Output: 0
```

### Notes

- Any number to the power of 0 equals 1: `power(x, 0) == 1`
- Any number to the power of 1 equals itself: `power(x, 1) == x`
- Zero to any positive power equals 0: `power(0, n) == 0` (when n > 0)
- Uses iterative multiplication for calculation
- Exponent must be a non-negative integer

---

## factorial

```python
def factorial(n: int) -> Union[int, str]
```

Calculates the factorial of a non-negative integer using iterative calculation.

### Parameters

- **n** (`int`): Non-negative integer to calculate factorial for

### Returns

- `int`: The factorial of n (n!)
- `str`: Error message if n is negative

### Error Handling

Returns the string `"Error: Factorial not defined for negative numbers"` when n is negative.

### Mathematical Definition

- `factorial(0) = 1`
- `factorial(n) = n × (n-1) × (n-2) × ... × 2 × 1`

### Examples

```python
from calculator import factorial

# Basic factorial
result = factorial(5)
print(result)  # Output: 120

# Factorial of zero
result = factorial(0)
print(result)  # Output: 1

# Factorial of one
result = factorial(1)
print(result)  # Output: 1

# Large factorial
result = factorial(10)
print(result)  # Output: 3628800

# Negative number (error case)
result = factorial(-5)
print(result)  # Output: "Error: Factorial not defined for negative numbers"
```

### Notes

- Factorial of 0 and 1 both equal 1
- Factorial grows very rapidly: `factorial(20) = 2,432,902,008,176,640,000`
- Uses iterative calculation (not recursive)
- Only defined for non-negative integers
- Check return type to handle error cases: `isinstance(result, str)`

### Common Factorial Values

| n | factorial(n) |
|---|--------------|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5,040 |
| 8 | 40,320 |
| 9 | 362,880 |
| 10 | 3,628,800 |

---

## Type Hints

All functions include complete type hints for better IDE support and type checking:

```python
from typing import Union

def add(a: float, b: float) -> float: ...
def subtract(a: float, b: float) -> float: ...
def multiply(a: float, b: float) -> float: ...
def divide(a: float, b: float) -> Union[float, str]: ...
def power(base: float, exponent: int) -> float: ...
def factorial(n: int) -> Union[int, str]: ...
```

## Error Handling Best Practices

When using functions that can return error strings (`divide` and `factorial`), always check the return type:

```python
from calculator import divide, factorial

# Check division result
result = divide(10, 0)
if isinstance(result, str):
    print(f"Error occurred: {result}")
else:
    print(f"Result: {result}")

# Check factorial result
result = factorial(-5)
if isinstance(result, str):
    print(f"Error occurred: {result}")
else:
    print(f"Result: {result}")
```

## Package Information

- **Package Name**: calculator
- **Version**: 1.0.0
- **Python Version**: 3.8+
- **License**: MIT