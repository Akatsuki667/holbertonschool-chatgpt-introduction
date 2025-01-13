#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Function description:
    This function computes the factorial of a non-negative integer using recursion. 
    The factorial of 0 is defined as 1, and for any positive integer n, 
    it is the product of all positive integers less than or equal to n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the given number n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Main program
# Read the first command-line argument, convert it to an integer, and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)  # Print the result