#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer.

    Function Description:
    This function calculates the factorial of a given non-negative integer n
    using a recursive approach. The factorial of a number n (denoted as n!) 
    is the product of all positive integers less than or equal to n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the integer from command-line arguments
f = factorial(int(sys.argv[1]))
print(f)