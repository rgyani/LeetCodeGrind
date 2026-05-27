"""
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter
so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.



Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Intuition: we just scan from left, find the first character which is not 'a' and replace it with 'a'?
however, what if we have "aba" -> "aaa" which is still a palindrome
 what if we have "aaa" -> ???


Instead, since it is a palindrome, loop the first half of the string, find first character not 'a', change to 'b' and return
if the loop finishes, we are still around, change the last character to 'b' and return

"""


def break_palindrome(palindrome: str) -> str:
    n = len(palindrome)
    if n <= 1:
        return ""

    # Convert to list since strings are immutable in Python
    s = list(palindrome)

    # Only scan the first half
    for i in range(n // 2):
        if s[i] != 'a':
            s[i] = 'a'
            return "".join(s)

    # If we get here, the string is all 'a's (e.g., "aaa" or "a")
    # Change the last character to 'b'
    s[-1] = 'b'
    return "".join(s)


if __name__ == "__main__":
    assert break_palindrome("abccba")  == "aaccba"
    assert break_palindrome("a")  == ""
    assert break_palindrome("aba")  == "abb"
    assert break_palindrome("abba")  == "aaba"
