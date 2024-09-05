!/usr/bin/python3


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers where each integer represents 1
        byte
                          (8 least significant bits) of data.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, otherwise False.

    UTF-8 Encoding Rules:
    - A UTF-8 character can be 1 to 4 bytes long.
    - The first byte determines how many bytes are used for the character.
    - For characters represented by more than 1 byte, the first byte has a
    specific bit pattern
      and subsequent bytes (continuation bytes) start with `10`.

    Byte Patterns:
    - 1-byte character: 0xxxxxxx (7 bits for the character)
    - 2-byte character: 110xxxxx 10xxxxxx
    - 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
    - 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    Example:
        validUTF8([197, 130, 1]) returns True
        validUTF8([235, 140, 4]) returns False
    """

    num_bytes = 0  # Tracks how many continuation bytes are expected

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000: Mask for the most significant bit (MSB)
    mask2 = 1 << 6  # 01000000: Mask for the second most significant bit

    for byte in data:
        # Only consider the 8 least significant bits (ignore any higher bits)
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character (0xxxxxxx),invalid if MSBis1
                return False
        else:
            # Check if it's a valid continuation byte (starts with '10')
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If num_bytes is not zero, there are leftover continuation bytes needed
    return num_bytes == 0
