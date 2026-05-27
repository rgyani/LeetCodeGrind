"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

Intuition:
Take left=0, right = len(s) -1
while left < right, if s[left] == s[right], left +=1, right -= 1
else, we can skip left or skip right, check both conditions (since u can skip only once)

##TODO what if u could skip n characters. DP approach
"""


def valid_palindrome(s: str) -> bool:
    if not s:
        return False

    # we simply start scanning from left and right,
    # if characters match, we are good,
    # if characters do not match try skipping either the left OR the right character

    def is_palindrome_range(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # When a mismatch occurs, try skipping either the left OR the right character
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)

    return True

if __name__ == "__main__":
    assert valid_palindrome("aba") == True
    assert valid_palindrome("aa") == True
    assert valid_palindrome("abc") == False
    assert valid_palindrome("abca") == True
    assert valid_palindrome("eedede") == True
