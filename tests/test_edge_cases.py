"""Edge case and error handling tests for calculator functions."""

import pytest

from calculator import add, divide, factorial, multiply, power, subtract


class TestDivisionEdgeCases:
    """Edge case tests for division function."""

    def test_divide_by_zero_returns_error_string(self) -> None:
        """Test that division by zero returns a string error message."""
        result = divide(10, 0)
        assert isinstance(result, str)
        assert result == "Error: Division by zero"

    def test_divide_zero_by_number(self) -> None:
        """Test that zero divided by any number returns zero."""
        assert divide(0, 5) == 0.0
        assert divide(0, 100) == 0.0
        assert divide(0, -7) == 0.0

    def test_divide_negative_by_negative(self) -> None:
        """Test division of two negative numbers."""
        assert divide(-10, -2) == 5.0

    def test_divide_float_precision(self) -> None:
        """Test division with float precision edge cases."""
        result = divide(1, 3)
        assert abs(result - 0.3333333333333333) < 1e-10

        result = divide(2, 3)
        assert abs(result - 0.6666666666666666) < 1e-10


class TestFactorialEdgeCases:
    """Edge case tests for factorial function."""

    def test_factorial_negative_returns_error_string(self) -> None:
        """Test that factorial of negative number returns error string."""
        result = factorial(-1)
        assert isinstance(result, str)
        assert result == "Error: Factorial not defined for negative numbers"

        result = factorial(-100)
        assert isinstance(result, str)
        assert "Error" in result

    def test_factorial_boundary_values(self) -> None:
        """Test factorial at boundary values 0 and 1."""
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_large_numbers(self) -> None:
        """Test factorial with large numbers."""
        assert factorial(15) == 1307674368000
        assert factorial(20) == 2432902008176640000

    def test_factorial_sequential(self) -> None:
        """Test that factorial(n+1) = factorial(n) * (n+1)."""
        for n in range(1, 10):
            assert factorial(n + 1) == factorial(n) * (n + 1)


class TestPowerEdgeCases:
    """Edge case tests for power function."""

    def test_power_zero_base(self) -> None:
        """Test power with zero as base."""
        assert power(0, 1) == 0
        assert power(0, 5) == 0
        assert power(0, 100) == 0

    def test_power_zero_exponent(self) -> None:
        """Test that any base to power 0 equals 1."""
        assert power(0, 0) == 1
        assert power(5, 0) == 1
        assert power(100, 0) == 1
        assert power(-5, 0) == 1

    def test_power_one_base(self) -> None:
        """Test that 1 to any power equals 1."""
        assert power(1, 0) == 1
        assert power(1, 1) == 1
        assert power(1, 100) == 1

    def test_power_large_exponents(self) -> None:
        """Test power with large exponents."""
        assert power(2, 20) == 1048576
        assert power(10, 6) == 1000000


class TestMultiplicationEdgeCases:
    """Edge case tests for multiplication function."""

    def test_multiply_by_zero(self) -> None:
        """Test multiplication by zero."""
        assert multiply(0, 0) == 0
        assert multiply(1000000, 0) == 0
        assert multiply(0, 1000000) == 0
        assert multiply(-5, 0) == 0

    def test_multiply_negative_numbers(self) -> None:
        """Test multiplication with negative numbers."""
        assert multiply(-5, -5) == 25
        assert multiply(-10, 3) == -30
        assert multiply(10, -3) == -30

    def test_multiply_large_numbers(self) -> None:
        """Test multiplication with large numbers."""
        assert multiply(1000, 1000) == 1000000
        assert multiply(999999, 1) == 999999

    def test_multiply_decimal_precision(self) -> None:
        """Test multiplication with decimal numbers."""
        result = multiply(0.1, 0.2)
        assert abs(result - 0.02) < 1e-10


class TestAdditionEdgeCases:
    """Edge case tests for addition function."""

    def test_add_large_numbers(self) -> None:
        """Test addition with very large numbers."""
        assert add(1000000, 2000000) == 3000000
        assert add(999999999, 1) == 1000000000

    def test_add_negative_numbers(self) -> None:
        """Test addition with negative numbers."""
        assert add(-5, -5) == -10
        assert add(-100, -200) == -300

    def test_add_mixed_signs(self) -> None:
        """Test addition with mixed positive and negative numbers."""
        assert add(10, -5) == 5
        assert add(-10, 5) == -5
        assert add(100, -100) == 0

    def test_add_decimal_precision(self) -> None:
        """Test addition with decimal numbers."""
        result = add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10


class TestSubtractionEdgeCases:
    """Edge case tests for subtraction function."""

    def test_subtract_same_number(self) -> None:
        """Test subtracting a number from itself."""
        assert subtract(5, 5) == 0
        assert subtract(100, 100) == 0
        assert subtract(-7, -7) == 0

    def test_subtract_larger_from_smaller(self) -> None:
        """Test subtracting larger number from smaller."""
        assert subtract(5, 10) == -5
        assert subtract(0, 100) == -100

    def test_subtract_negative_numbers(self) -> None:
        """Test subtraction with negative numbers."""
        assert subtract(-5, -10) == 5
        assert subtract(-10, -5) == -5

    def test_subtract_decimal_precision(self) -> None:
        """Test subtraction with decimal numbers."""
        result = subtract(0.3, 0.1)
        assert abs(result - 0.2) < 1e-10


class TestTypeConsistency:
    """Test type consistency across all functions."""

    def test_add_returns_numeric(self) -> None:
        """Test that add always returns a numeric type."""
        result = add(1, 2)
        assert isinstance(result, (int, float))

    def test_subtract_returns_numeric(self) -> None:
        """Test that subtract always returns a numeric type."""
        result = subtract(5, 3)
        assert isinstance(result, (int, float))

    def test_multiply_returns_numeric(self) -> None:
        """Test that multiply always returns a numeric type."""
        result = multiply(2, 3)
        assert isinstance(result, (int, float))

    def test_divide_returns_float_or_string(self) -> None:
        """Test that divide returns float or error string."""
        result = divide(10, 2)
        assert isinstance(result, (float, str))

        result = divide(10, 0)
        assert isinstance(result, str)

    def test_power_returns_numeric(self) -> None:
        """Test that power returns a numeric type."""
        result = power(2, 3)
        assert isinstance(result, (int, float))

    def test_factorial_returns_int_or_string(self) -> None:
        """Test that factorial returns int or error string."""
        result = factorial(5)
        assert isinstance(result, (int, str))

        result = factorial(-1)
        assert isinstance(result, str)

# Made with Bob
