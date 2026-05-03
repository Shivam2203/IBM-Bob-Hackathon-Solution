#!/usr/bin/env python3
"""
Example usage of the calculator module.
Demonstrates all available operations and error handling.
"""

from calculator import add, subtract, multiply, divide, power, factorial


def main():
    print("=" * 60)
    print("Calculator Module - Usage Examples")
    print("=" * 60)
    
    # Addition examples
    print("\n1. ADDITION")
    print("-" * 40)
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"add(-10, 15) = {add(-10, 15)}")
    print(f"add(2.5, 3.7) = {add(2.5, 3.7)}")
    
    # Subtraction examples
    print("\n2. SUBTRACTION")
    print("-" * 40)
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"subtract(5, 8) = {subtract(5, 8)}")
    print(f"subtract(-3, -7) = {subtract(-3, -7)}")
    
    # Multiplication examples
    print("\n3. MULTIPLICATION")
    print("-" * 40)
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"multiply(-4, 5) = {multiply(-4, 5)}")
    print(f"multiply(2.5, 4) = {multiply(2.5, 4)}")
    
    # Division examples (with error handling)
    print("\n4. DIVISION")
    print("-" * 40)
    print(f"divide(20, 4) = {divide(20, 4)}")
    print(f"divide(7, 2) = {divide(7, 2)}")
    
    # Division by zero - returns error string
    result = divide(10, 0)
    if isinstance(result, str):
        print(f"divide(10, 0) = {result}")
    else:
        print(f"divide(10, 0) = {result}")
    
    # Power examples
    print("\n5. POWER")
    print("-" * 40)
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"power(5, 0) = {power(5, 0)}")
    print(f"power(10, 2) = {power(10, 2)}")
    
    # Factorial examples (with error handling)
    print("\n6. FACTORIAL")
    print("-" * 40)
    print(f"factorial(5) = {factorial(5)}")
    print(f"factorial(0) = {factorial(0)}")
    print(f"factorial(10) = {factorial(10)}")
    
    # Factorial with negative number - returns error string
    result = factorial(-5)
    if isinstance(result, str):
        print(f"factorial(-5) = {result}")
    else:
        print(f"factorial(-5) = {result}")
    
    # Complex calculation example
    print("\n7. COMPLEX CALCULATION")
    print("-" * 40)
    print("Calculate: (5 + 3) * 2^3 / 4")
    step1 = add(5, 3)
    step2 = power(2, 3)
    step3 = multiply(step1, step2)
    result = divide(step3, 4)
    print(f"Result: {result}")
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

# Made with Bob
