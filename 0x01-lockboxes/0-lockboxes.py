#!/usr/bin/python3
"""
Module for determining if all the boxes can be unlocked.
Each box may contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes
                      and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
