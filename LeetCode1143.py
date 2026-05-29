"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Intuition: Best explained in this video: https://www.youtube.com/watch?v=NnD96abizww
A better example is longest common subsequence of abcdef and acbcf is abcf

    a b c d a f
  0 0 0 0 0 0 0
a 0 1 1 1 1 1 1
c 0 1 1 2 1 1 1
b 0 1
c 0
f 0

in each comparison, we are comparing
if s[i] == s[j], then dp[i][j] = 1+ dp[i-1][j-1]
else dp[i][j] = max(dp[i-1][j], dp[i][j-1])
 """

def longest_common_subsequence(text1:str, text2:str)->int :
    if not text1 or not text2:
        return 0

    m = len(text2)
    n = len(text1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text2[i - 1] == text1[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("abcdef", "acbcf ") == 4
    assert longest_common_subsequence("bsbininm", "jmjkbkjkv") == 1