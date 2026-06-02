"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.


Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.


Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true


Intuiton: why cant we take three pointers p1, p2, p3
if p1 == p3, increment both
else if p2 == p3, increment both
else return False

because this approach is greedy towards p1, since we always compre p3 with p1 first, this will break on 1st example

Instead we will create a grid path where row represents characters of s1, while cols represent characters of s2
if we move left, we interleave s2 while if we move down, we interleave s1

At each position we just check if we consume all characters is interleaving possible
so if  (dp[i-1][j] and s1[i] == s3[i+j]) or (dp[i][j-1] and s2[j] == s3[i+j])
X = empty
  X  d  b  b  c  a
X T  F  F  F  F  F   <- if s1 was empty
a T  F  F  F  F  F
a T  T  T  T  T  T
b F  T  T  F  T  F
c F  F  T  T  T  T
c F  F  F  T  F  T
"""


def interleave_possible(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)

    if m + n != len(s3):
        return False

    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    # fill the first row when s2 is empty
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    # fill the first column when s1 is empty
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            top = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            left = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            dp[i][j] = top or left

    return dp[m][n]


if __name__ == "__main__":
    assert interleave_possible(s1="aabcc", s2="dbbca", s3="aadbbcbcac") == True
    assert interleave_possible(s1="aabcc", s2="dbbca", s3="aadbbbaccc") == False
    assert interleave_possible("", "", "") == True
