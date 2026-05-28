"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and
chooses the element in the next row that is either directly below or diagonally left/right.

Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13

Explanation: There are two falling paths [1,5,7] and [1,4,8]


Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is [-19, -40]


Intuition: u obviously cant choose the smallest number and start from there
Instead we should run thru the full grid, find smallest path to reach this particular index
Then in the last row, we find the shortest path

"""
from math import inf


def min_falling_path_sum(matrix: list[list[int]]) -> int:
    m = len(matrix)
    n=len(matrix[0])

    # I prefer to initialize the dp array with buffers so that the if conditions become simpler
    dp = [[inf] * (n+2) for _ in range(m+1)]
    dp[0] = [0] * (n+2)

    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i-1][j-1]

    return int(min(dp[m]))

if __name__ == "__main__":
    assert min_falling_path_sum([[2,1,3],[6,5,4],[7,8,9]]) == 13
    assert min_falling_path_sum([[-19,57],[-40,-5]]) == -59