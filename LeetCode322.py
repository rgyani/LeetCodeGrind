"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Intution: for coins = [1,2,5], amount = 11 can be reached by adding 1 coin to 10, or 2 coin to 9, or 5 coin to 6
we can find which one has least amount of coins

so using DP approach, we can maintain an array where each element contains the minimum coins needed to reach this
so dp[0] = 0, dp[1] = 1, dp[2] = min(dp[1] + 1, 1), dp[3] = min(dp[2] + 1, dp[0] + 1), dp[4] = min(dp[2] + 1, dp[3] + 1), dp[5] = min(1, dp[3] + 2, dp[4]+1) and so on
do dp[n] = min(dp[n-1] + 1, dp[n-2] + 1, dp[n-5] + 1)


   0  1  2  3  4  5  6  7  8  9  10  11
1  0  1  2  3  4  5  6  7  8  9  10  11
2  0  1  1  2  2  3  3  4  4  5  5   6
5  0  1  1  1  1  1  2  2  3  3  2   3
"""
from math import inf


def coin_change(coins:list[int], amount:int)-> int:
    if amount == 0:
        return 0

    # dp[i] will be storing the minimum number of coins required for amount i
    # amount + 1 is a placeholder for infinity
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    assert coin_change([1,2,5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
