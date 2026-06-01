"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Onput: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Intution: Keep it simple stupid, left = 0, right = n-1
while left <right if valid[left] == valid[right] keep on, else return false

"""
import re


def is_palindrome(s:str)-> bool:
    s = [ch for ch in s.lower() if ch.isalnum()]

    if len(s) == 0:
        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left +=1
            right -=1
        else:
            return False

    return True

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert  is_palindrome("race a car") == False
    assert is_palindrome("  ") == True