"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Intuition:
set x = input, y = 0
till x != 0, y = y*10 + x % 10, x = x // 10
compare y and input
"""


def is_palindrome(input: int) -> bool:
    if input < 0:
        return False

    x = input
    y = 0

    # just reverse the number by continously doing a moduly of 10 and compare the result
    while x != 0:
        y = y * 10 + x % 10
        x //= 10

    return input == y


if __name__ == "__main__":
    assert is_palindrome(123) == False
    assert is_palindrome(121) == True
    assert is_palindrome(-121) == False
    assert is_palindrome(10) == False
    assert is_palindrome(0) == True
