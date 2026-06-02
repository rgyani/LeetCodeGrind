"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Intuition:
Remember In a normal string, palindromic substrings can be of odd or even length:

To Solve it using DP approach, we build a DP array, where dp[i][j] tells u where s[i][j] is a palindrome
dp[i][i] = true since it is a palindrome of length 1
dp[i][j] = true when s[i:j] is a palindrome, ie if s[i] == s[j] and dp[i+1][j-1] == true

Since we are using dp[i+1] for getting value of dp[i], we need reverse iterate 'i's
  b  a  b  a  d
  0  1  2  3  4
0 T  F  T  F  F
1    T  F  T  F
2       T  F  F
3          T  F
4             T

  c  b  b  d
  0  1  2  3
0 T  F  F  F
1    T  T  F
2       T  F
3          T
This is brute force approach
1. Can not be improved with DP apprach
1. Can be improved with Manacher's algo https://www.youtube.com/watch?v=V-sEwsca1ak
"""


def longest_palindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    dp = [[False] * n for _ in range(n)]

    start = 0
    max_len = 1

    for i in range(n):
        dp[i][i] = True

    # i moves backward,  j moves forward
    for i in range(n-1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j] and (j-i == 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if max_len <= j - i + 1:
                    max_len = j - i + 1
                    start = i

    return s[start:max_len + start]


if __name__ == "__main__":
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("babad") == "bab"
    assert longest_palindrome("raceacar") == "aca"

    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
