#!/usr/bin/python3
"""N Queens Algorithm with Backtracking (Recursion inside loop)"""

import sys


class NQueen:
    """Class for solving the N Queen Problem"""

    def __init__(self, n):
        """Initialize the board size and solution storage."""
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """
        Check if the k-th queen can be placed in column i.

        Args:
            k (int): The k-th queen to be placed.
            i (int): The column in which to place the queen.

        Returns:
            bool: True if the queen can be placed, False otherwise.
        """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def nQueen(self, k):
        """
        Try to place every queen on the board.

        Args:
            k (int): The starting queen index to evaluate (should be 1).

        Returns:
            list: A list of all the solutions.
        """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = []
                    for j in range(1, self.n + 1):
                        solution.append([j - 1, self.x[j] - 1])
                    self.res.append(solution)
                else:
                    self.nQueen(k + 1)
        return self.res


def main():
    """Main function to execute the N Queen solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = NQueen(N)
    res = queen.nQueen(1)

    for solution in res:
        print(solution)


if __name__ == "__main__":
    main()
