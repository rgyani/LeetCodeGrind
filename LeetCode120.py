"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11

Example 2:

Input: triangle = [[-10]]
Output: -10


  -1
  3 2
-3 1 -1

    2
   3 4
  6 5 7
 4 1 8 3
4 1 8 3 4

Intuition:
dp[i][j] += min(dp[i-1][j], dp[i-1][j-1]) if j != len(current row)
"""
from math import inf


def minimum_total(triangle: list[list[int]]) -> int:
    n = len(triangle[-1])

    # dp[col] will store the min path sum to that column
    # Pad with inf, but set the virtual "start" to 0
    dp = [inf] * (n + 1)
    dp[1] = triangle[0][0] # Initialize with the top element

    # Start from the second row
    for lst in triangle[1:]:
        # Loop backwards so we don't overwrite values we need to read
        for j in range(len(lst) - 1, -1, -1):
            # j+1 in our 1-indexed DP array maps to index j in the triangle
            dp[j + 1] = lst[j] + min(dp[j], dp[j + 1])

    return min(dp)

if __name__== "__main__":
    assert minimum_total([[-1],[3,2],[-3,1,-1]]) == -1
    assert minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11
    assert minimum_total([[-10]]) == -10
    assert minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11
