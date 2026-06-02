"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Intuition:

X = blank

   X  r  o  s
X  0  1  2  3
h  1  1  2  3
o  2  2  1  2
r  3  2  2  2
s  4  3  3
e  5

from blank to blank cost is 0
from blank to r cost is 1, ro is 2, ros is 3
from h to empty cost is 1, from h to r cost is again 1, ro is 2 and ros is 3

if we had a blank output string, we wud have paid the cost = num of characters in word1
say we had
h and r,     we would have paid 1 cost,
ho and r,    we would have paid 1+1 cost
hor and r,   since we already paid cost to convert ho to blank of 2, we dont pay anything else

if we had ho and ro, the cost is conversion of h to r
if we had hor and r, the cost is conversion of ho to blank

if we get matching characters, we just copy dp[i-1][j-1], ie the cost of prefixes before these characters
if we dont, we find the minimum cost among dp[i-1][j-1], dp[i-1][j] and dp[i][j-1] and add 1 to it
"""


def min_distance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)

    # instead of making a full dp, lets keep only 2 rows, prev and current and toggle between them for each i
    # also keep an extra element at the left to ease calculations
    dp = [[i for i in range(n+1)] for _ in range(2)]

    current = 0
    for i in range(0, m):
        current = i % 2
        prev = (i + 1) % 2
        dp[current][0] = i + 1
        for j in range(0, n):
            if word1[i] == word2[j]:
                dp[current][j+1] = dp[prev][j]
            else:
                dp[current][j+1] = 1+ min(dp[prev][j], dp[current][j], dp[prev][j+1])

    return dp[current][n]

if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "") == 0
    assert min_distance("a", "") == 1
    assert min_distance("", "a") == 1
