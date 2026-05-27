"""
You are given an m x n integer array grid.
There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

# again simple DP summing the cell above and to the left at each position, just dont allow movement into the obstacle cell
Similar to LeetCode62.py
"""


def unique_paths_with_obstacles(obstacleGrid: list[list[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0

    if m == 1 and n == 1:
        return 1

    dp = [[0] * n for _ in range(m)]

    for i, v in enumerate(obstacleGrid):
        for j, val in enumerate(v):
            if val == 1:
                dp[i][j] = -1
            else:
                if i == 0 and j == 1:
                    dp[i][j] = 1
                elif i == 1 and j == 0:
                    dp[i][j] = 1
                else:
                    if i - 1 >= 0 and dp[i - 1][j] != -1:
                        dp[i][j] += dp[i - 1][j]
                    if j - 1 >= 0 and dp[i][j - 1] != -1:
                        dp[i][j] += dp[i][j - 1]

    return max(dp[m - 1][n - 1], 0)


if __name__ == "__main__":
    assert unique_paths_with_obstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert unique_paths_with_obstacles(obstacleGrid=[[0, 1], [0, 0]]) == 1
    assert unique_paths_with_obstacles(obstacleGrid=[[0, 1]]) == 0
    assert unique_paths_with_obstacles(obstacleGrid=[[0]]) == 1
