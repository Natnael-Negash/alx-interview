#!/usr/bin/python3
"""
Module for calculating the minimum number of coins needed to make change.
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to meet a given total.

    Args:
        coins (list): A list of the values of available coins.
        total (int): The total amount of change needed.

    Returns:
        int: The minimum number of coins needed to make the change,
             or -1 if it is not possible.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with 'inf' for all values from 1 to total
    # and 0 for the 0 value
    dp = [0] + [float("inf")] * total

    # Iterate through each coin
    for coin in coins:
        # Update the dp array for each value from the coin to the total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result for the total or -1 if it's not possible
    # to make the total
    return dp[total] if dp[total] != float("inf") else -1
