"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0


Intution: dp[i][j] == "1" it is a square of length atleast 1, but
if dp[i-1][j] is a square of length >1 and also dp[i][j-1] is a square of length > 1 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
if dp[i-1][j] is a square of length >1 and also dp[i][j-1] is a square of length > 1 and dp[i-1][j-1] == 1, then dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
"""
from math import sqrt
from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])

    # dp grid size (m+1) x (n+1) initialized to 0
    # This acts as a perfect safety buffer for row 0 and col 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_side = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Check the corresponding cell in the original matrix
            if matrix[i - 1][j - 1] == "1":
                # The core DP transition using side lengths
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    # Return the area
    return max_side * max_side

if __name__ == "__main__":
    assert maximal_square([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                           ["1", "0", "0", "1", "0"]]) == 4
    assert maximal_square([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                           ["1", "0", "1", "1", "1"]]) == 9

    assert maximal_square([["0", "1"], ["1", "0"]]) == 1
    assert maximal_square([["0"]]) == 0
    assert maximal_square([["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                           ["1", "1", "1", "1", "1"]]) == 16
    assert maximal_square([["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                           ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"]]) == 25