"""Unit tests for calculator functions."""

import pytest

from calculator import add, divide, factorial, multiply, power, subtract


class TestAddition:
    """Test cases for the add function."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (1.5, 2.5, 4.0),
            (-5, -3, -8),
            (100, 200, 300),
            (-10.5, 5.5, -5.0),
        ],
    )
    def test_add_various_inputs(self, a: float, b: float, expected: float) -> None:
        """Test addition with various input combinations."""
        assert add(a, b) == expected

    def test_add_large_numbers(self) -> None:
        """Test addition with large numbers."""
        assert add(1000000, 2000000) == 3000000

    def test_add_commutative(self) -> None:
        """Test that addition is commutative (a + b = b + a)."""
        assert add(5, 3) == add(3, 5)


class TestSubtraction:
    """Test cases for the subtract function."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (5, 3, 2),
            (0, 5, -5),
            (-3, -2, -1),
            (10.5, 5.5, 5.0),
            (100, 100, 0),
            (-10, -20, 10),
        ],
    )
    def test_subtract_various_inputs(self, a: float, b: float, expected: float) -> None:
        """Test subtraction with various input combinations."""
        assert subtract(a, b) == expected

    def test_subtract_large_numbers(self) -> None:
        """Test subtraction with large numbers."""
        assert subtract(5000000, 2000000) == 3000000

    def test_subtract_identity(self) -> None:
        """Test that subtracting zero returns the original number."""
        assert subtract(42, 0) == 42


class TestMultiplication:
    """Test cases for the multiply function."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (3, 4, 12),
            (0, 100, 0),
            (-2, 5, -10),
            (2.5, 4, 10.0),
            (-3, -4, 12),
            (1, 999, 999),
        ],
    )
    def test_multiply_various_inputs(self, a: float, b: float, expected: float) -> None:
        """Test multiplication with various input combinations."""
        assert multiply(a, b) == expected

    def test_multiply_by_zero(self) -> None:
        """Test that multiplying by zero returns zero."""
        assert multiply(12345, 0) == 0
        assert multiply(0, 12345) == 0

    def test_multiply_commutative(self) -> None:
        """Test that multiplication is commutative (a * b = b * a)."""
        assert multiply(7, 8) == multiply(8, 7)

    def test_multiply_identity(self) -> None:
        """Test that multiplying by one returns the original number."""
        assert multiply(42, 1) == 42


class TestDivision:
    """Test cases for the divide function."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (10, 2, 5.0),
            (7, 2, 3.5),
            (-10, 2, -5.0),
            (0, 5, 0.0),
            (100, 4, 25.0),
            (1, 3, 0.3333333333333333),
        ],
    )
    def test_divide_various_inputs(self, a: float, b: float, expected: float) -> None:
        """Test division with various input combinations."""
        result = divide(a, b)
        assert isinstance(result, float)
        assert abs(result - expected) < 1e-10

    def test_divide_by_zero(self) -> None:
        """Test that dividing by zero returns an error message."""
        result = divide(10, 0)
        assert isinstance(result, str)
        assert "Error" in result
        assert "Division by zero" in result

    def test_divide_identity(self) -> None:
        """Test that dividing by one returns the original number."""
        assert divide(42, 1) == 42.0

    def test_divide_self(self) -> None:
        """Test that dividing a number by itself returns 1."""
        assert divide(42, 42) == 1.0


class TestPower:
    """Test cases for the power function."""

    @pytest.mark.parametrize(
        "base,exponent,expected",
        [
            (2, 3, 8),
            (5, 0, 1),
            (10, 2, 100),
            (3, 4, 81),
            (2, 10, 1024),
            (7, 1, 7),
        ],
    )
    def test_power_various_inputs(
        self, base: float, exponent: int, expected: float
    ) -> None:
        """Test power function with various input combinations."""
        assert power(base, exponent) == expected

    def test_power_zero_exponent(self) -> None:
        """Test that any number to the power of 0 equals 1."""
        assert power(100, 0) == 1
        assert power(0, 0) == 1

    def test_power_one_exponent(self) -> None:
        """Test that any number to the power of 1 equals itself."""
        assert power(42, 1) == 42

    def test_power_base_zero(self) -> None:
        """Test that 0 to any positive power equals 0."""
        assert power(0, 5) == 0
        assert power(0, 100) == 0


class TestFactorial:
    """Test cases for the factorial function."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 1),
            (1, 1),
            (5, 120),
            (10, 3628800),
            (3, 6),
            (7, 5040),
        ],
    )
    def test_factorial_various_inputs(self, n: int, expected: int) -> None:
        """Test factorial with various input values."""
        assert factorial(n) == expected

    def test_factorial_negative(self) -> None:
        """Test that factorial of negative number returns error message."""
        result = factorial(-5)
        assert isinstance(result, str)
        assert "Error" in result
        assert "negative" in result

    def test_factorial_zero_and_one(self) -> None:
        """Test that factorial of 0 and 1 both equal 1."""
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_large_number(self) -> None:
        """Test factorial with a larger number."""
        assert factorial(20) == 2432902008176640000

# Made with Bob
