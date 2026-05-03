"""Calculator module providing basic arithmetic operations.

This module contains functions for performing common mathematical operations
including addition, subtraction, multiplication, division, exponentiation,
and factorial calculations.
"""

from typing import Union


def add(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: First number to add
        b: Second number to add

    Returns:
        The sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        The difference of a and b (a - b)

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(0, 5)
        -5
        >>> subtract(10.5, 5.5)
        5.0
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers together.

    Args:
        a: First number to multiply
        b: Second number to multiply

    Returns:
        The product of a and b

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(0, 100)
        0
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


def divide(a: float, b: float) -> Union[float, str]:
    """Divide the first number by the second.

    Args:
        a: Numerator (number to be divided)
        b: Denominator (number to divide by)

    Returns:
        The quotient of a and b, or an error message if b is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
        >>> divide(10, 0)
        'Error: Division by zero'
    """
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base: float, exponent: int) -> float:
    """Raise a base number to an exponent power.

    This function uses an iterative approach to calculate the power.

    Args:
        base: The base number
        exponent: The exponent (must be non-negative integer)

    Returns:
        The result of base raised to the power of exponent

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
        >>> power(10, 2)
        100
    """
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def factorial(n: int) -> Union[int, str]:
    """Calculate the factorial of a non-negative integer.

    This function uses an iterative approach to calculate the factorial.

    Args:
        n: Non-negative integer to calculate factorial for

    Returns:
        The factorial of n, or an error message if n is negative

    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(5)
        120
        >>> factorial(-5)
        'Error: Factorial not defined for negative numbers'
    """
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Made with Bob
