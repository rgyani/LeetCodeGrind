"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
"""


def max_coins(nums: list[int]) -> int:
    n = len(nums)

    # Pad the array with 1 at both ends
    a = [1] + nums + [1]

    # Initialize the DP table with zeros
    # Size is (n + 2) x (n + 2)
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    # Matrix Chain Multiplication (MCM) style DP
    for length in range(n):
        for i in range(1, n - length + 1):
            j = i + length
            for k in range(i, j + 1):
                # dp[i][k-1] + dp[k+1][j] + coin gained from bursting balloon k last
                coins = dp[i][k - 1] + dp[k + 1][j] + a[k] * a[i - 1] * a[j + 1]
                dp[i][j] = max(dp[i][j], coins)

    return dp[1][n]

if __name__ == "__main__":
    assert max_coins([3,1,5,8]) == 167
    assert max_coins([1,5]) == 10