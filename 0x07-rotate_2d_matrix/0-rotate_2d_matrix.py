#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise.

    Args:
        matrix (list of list of int): 2D matrix to be rotated.

    Returns:
        None: The matrix is rotated in place.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save the top element
            top = matrix[first][i]
            # Move left element to top
            matrix[first][i] = matrix[last - offset][first]
            # Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Move top element to right
            matrix[i][last] = top

# Alternative approach to rotate the 2D matrix 90 degrees clockwise
# def rotate_2d_matrix(matrix):
#     n = len(matrix)
#     # Transpose the matrix (swap rows with columns)
#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     # Reverse the rows to complete the rotation
#     for i in range(n):
#         matrix[i].reverse()
