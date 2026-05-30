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
Keep it simple stupid, iterate thru the list, check palindrome on either side with this element as center or with this element as part of palindrome
keep noting the palindrome size at each step
return the max of possible palindromes

This is brute force approach
1. Can not be improved with DP apprach
1. Can be improved with Manacher's algo https://www.youtube.com/watch?v=V-sEwsca1ak
"""


def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    ## keep it simple stupid expand left and right along each index, find largest palindrone and return

    def expand(left:int, right:int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    start, end = 0, 0

    for i in range(len(s)):
        # there could be a palindrome around this character
        l, r = expand(i, i)

        if r - l > end - start:
            start, end = l, r

        # there could be a palindrome containing this character
        l, r = expand(i, i+1)
        if r - l > end - start:
            start, end = l, r

    return s[start: end + 1]


if __name__ == "__main__":
    assert longest_palindrome("babad") == "bab"
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("raceacar") == "aca"

    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
