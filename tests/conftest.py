"""Pytest configuration and fixtures for calculator tests."""

import pytest
from typing import Callable, Dict

from calculator import add, divide, factorial, multiply, power, subtract


@pytest.fixture
def calculator_functions() -> Dict[str, Callable]:
    """Provide all calculator functions for testing.

    Returns:
        Dictionary mapping function names to function objects
    """
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "power": power,
        "factorial": factorial,
    }


@pytest.fixture
def sample_numbers() -> Dict[str, float]:
    """Provide sample numbers for testing.

    Returns:
        Dictionary of sample numbers for various test scenarios
    """
    return {
        "positive": 10.0,
        "negative": -5.0,
        "zero": 0.0,
        "decimal": 3.14,
        "large": 1000000.0,
    }

# Made with Bob
