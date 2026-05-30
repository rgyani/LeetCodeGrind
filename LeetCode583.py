"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.


Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Institution:
As you iterate over the row, if u have word1[i] != word2[j], u can delete from either words, ie min(dp[i-1][j], dp[i][j-1]) + 1
if characters are same, u dont need to delete anything, but cost will be dp[i-1][j-1]

where X = empty

  X e a t
X 0 1 2 3
s 1 2 3 4
e 2 1 2 3
a 3 2 1 2


  X e t c o
X 0 1 2 3 4
l 1 2 3 4 5
e 2 1 2 3 4
e 3 2 3 4 5
t 4 3 2 3 5
c 5 4 3 2 3
o 6 5 4 3 2
d 7 6 5 4 3
e 8 7 6 5 4
"""

def min_distance(word1:str, word2:str) -> int:
    m = len(word1)
    n = len(word2)

    # we only need 2 rows of DP current and prev
    # 1 extra column for easy if condition where col == 0
    dp = [[i for i in range(n+1)] for _ in range(2)]

    current = 0
    for i in range(1, m+1):
        current = i%2
        prev = (i+1)%2
        dp[current][0] = i
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[current][j] = dp[prev][j-1]
            else:
                dp[current][j] = 1 + min(dp[prev][j], dp[current][j-1])

    return dp[current][n]

if __name__ == "__main__":
    assert min_distance(word1 = "sea", word2 = "eat") == 2
    assert min_distance(word1 = "leetcode", word2 = "etco") == 4
    assert min_distance(word1="ac", word2="def") == 5
    assert min_distance(word1="", word2="d") == 1
    assert min_distance(word1="", word2="") == 0


