"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Intuition: again screams DP since dp[i][j] = min(dp[i-1][j], dp[i][j-1])
"""
from math import inf
from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    # to keep things simple we add buffer of 0 to both left and top sides
    dp = [[inf] * (n+1) for _ in range(m+1)]

    dp[0][0] = dp[1][0]= dp[1][1] = 0
    for i, lst in enumerate(grid):
        for j, val in enumerate(lst):
            dp[i+1][j+1] = val + min(dp[i][j+1], dp[i+1][j])

    return dp[m][n]

if __name__ == "__main__":
    assert min_path_sum([[100, 100, 100, 100]]) == 400
    assert min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) == 7
    assert min_path_sum([[1,2,3],[4,5,6]]) == 12
