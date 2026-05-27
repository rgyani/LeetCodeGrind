"""
There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).

The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.


Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3

Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

|S| |
| | |
| |E|


Intuition: This screams DP, since to get to E, u need to be on above cell, ie. dp[m-2][n-1] or left: dp[m-1][n-2] cell
"""
def unique_paths(m:int, n:int)-> int:
    if m <= 1 or n <= 1:
        return 1

    # to keep calculations simple lets set an extra buffer row and col on left and right
    # cant use dp = [[0] * (n+1)] * (m+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    dp[1][1] = 0 # start pos
    dp[1][2] = 1 # first right move
    dp[2][1] = 1 # first down move

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i][j], dp[i-1][j] + dp[i][j-1])

    return dp[m][n]

if __name__ == "__main__":
    assert unique_paths(3, 2) == 3
    assert unique_paths(3,7) == 28
