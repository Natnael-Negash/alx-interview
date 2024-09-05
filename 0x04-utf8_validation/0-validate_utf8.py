#!/usr/bin/python3
"""
UTF-8 Validation Module

This module contains a function to validate if a given data set
is encoded in valid UTF-8.
"""


def validUTF8(data) -> bool:
    """
    Checks if the given data set is a valid UTF-8 encoding.
    Args:
        data (list): A list of integers representing bytes of data.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        mask = 1 << 7

        if num_bytes == 0:
            # Count the number of leading 1's
            # to determine the number of bytes in the character
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            # If no leading 1's, it's a single-byte character (0xxxxxxx)
            if num_bytes == 0:
                continue

            # UTF-8 encoding can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the following bytes start with 10xxxxxx
            if byte >> 6 != 0b10:
                return False

        num_bytes -= 1
# All characters should be fully processed by the end
    return num_bytes == 0
