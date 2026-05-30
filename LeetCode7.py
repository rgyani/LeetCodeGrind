"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Intution: simply take the abs value of x and keep adding result = result * 10 + x %10 and x//=10
however this will fail if  x = 1,534,236,469, its reverse 9,646,324,351 is greater than max signed 32 bit number
"""

def reverse(x:int)->int:
    result = 0
    MAX_INT = 2**31 - 1

    mult = -1 if x < 0 else 1
    x = abs(x)  # x%10 wont work as expected for x<0
    while x != 0:
        result = result * 10 + x%10
        x//=10

        if result > MAX_INT:
            return 0

    return result * mult

if __name__ == "__main__":
    assert reverse(-123) == -321
    assert reverse(123) == 321
    assert reverse(120) == 21