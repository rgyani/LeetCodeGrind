"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Intitution:
For any number the result(n) be min(result(n-1) + 1, result(n-4) + 1, result(n-9) + 1)....)
so for each step, we calculate the possible combinations using all perfect squares
"""


def num_squares(n: int) -> int:
    # Initialize the DP table with a maximum possible value (n)
    # dp[i] will store the least number of perfect squares that sum to i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Build up solutions from 1 to n
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return int(dp[n])


if __name__ == "__main__":
    assert num_squares(12) == 3
    assert num_squares(13) == 2