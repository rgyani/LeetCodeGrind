"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.


Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Intution:
Consider mbadm
 We look at the two ends, i = 0, j= 4, s[i] == s[j], we now compare s[i+1] and s[j+1]
now these dont match, so how do i make them happy. either insert s[j] on the left or insert s[i] on the right

so bad becomes either
1. dbad      d we added, so now we solve ba, ie s[i..j-1] which is dp[i][j-1]
2. or badb   b we added, so now we solve ad, ie s[i+1...j] which is dp[i+1][j]
so dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

Choice 1: fixed right end (j), shrink j inward → dp[i][j-1]
Choice 2: fixed left end (i), shrink i inward  → dp[i+1][j]

"""


def min_insertions(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # fill by increasing length
    #  length 2 first, then 3, then 4...
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

if __name__ == "__main__":
    assert min_insertions("zzazz") == 0
    assert min_insertions("mbadm") == 2
    assert min_insertions("leetcode") == 5