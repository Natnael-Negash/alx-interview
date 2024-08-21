#!/usr/bin/python3
"""Module for calculating the minimum number of operations."""


def minOperations(n):
    """
    Calculates the minimum number of operations needed
    to result in exactly n 'H' characters.
    Args:
        n (int): The desired number of 'H' characters.
    Returns:
        int: The minimum number of operations.
    """
    # Ensure that the input is at least 2 characters long
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # Check if n is evenly divisible by root
        if n % root == 0:
            # Increment the total number of operations by root
            ops += root
            # Set n to the quotient after division by root
            n = n / root
            # Decrement root to find smaller values that evenly divide n
            root -= 1
        # Increment root until it reaches a value that evenly divides n
        root += 1
    return ops
