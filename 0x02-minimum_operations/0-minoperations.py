#!/usr/bin/python3

def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly n 'H' characters in the file.

    Operations:
    - Copy All: Copy all the 'H' characters present in the file.
    - Paste: Paste the characters copied.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed to achieve exactly n 'H' characters.
         If n is impossible to achieve (i.e., n <= 1), returns 0.
    """
    # Ensure that the input is at least 2 characters long
    if (n < 2):
        return 0
    
    operations = 0
    divisor = 2

    while divisor <= n:

        if n % divisor == 0:
            operations += divisor
            n = n / divisor
            divisor -= 1
        divisor += 1

    return operations