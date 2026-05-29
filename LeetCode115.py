"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

Intuition

X = blank
   X  r  a  b  b  i  t
X  1  0  0  0  0  0  0
r  1  1  0  0  0  0  0
a  1  1  1  0  0  0  0
b  1  1  1  1  0  0  0
b  1  1  1  2* 2+ 0  0          *dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
b  1  1  1  2  3  0  0
i  1  1  1  2  3  3  0
t  1  1  1  2  3  3  3

I scan row by row in the source string.
At each step, I look up to see what I could have made without this current character (since from source string i have the option to use this character or drop it)
, and I look diagonally to see what I can make by including it."

dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

"""


def num_distinct(s: str, t: str) -> int:
    m = len(s)
    n = len(t)
    # we simply need previous row and current row,
    # so no use creating the full dp array, just two rows for current and prev wud do
    # Plus 1 extra col for easy calculations
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][0] = 1  # blanks match

    current = 0
    for i in range(1, m + 1):
        current = i % 2
        prev = (i + 1) % 2

        dp[current][0] = 1 # empty t matches

        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[current][j] = dp[prev][j - 1] + dp[prev][j]
            else:
                dp[current][j] = dp[prev][j]

    return dp[current][n]


if __name__ == "__main__":
    # assert num_distinct(s="ccc", t="c") == 3
    assert num_distinct(s="rabbbit", t="rabbit") == 3
    assert num_distinct(s="babgbag", t="bag") == 5
    assert num_distinct("", "") == 1
    assert num_distinct("abc", "def") == 0
