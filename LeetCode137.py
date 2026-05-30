"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

Intuition:
If duplicates appear... Your mental model is...       The tool you use is...
2 times (Even)          Flip-flop switch (2 states)   XOR (^)
K times                 Rotary dial (K states)      Bitwise Column Sum % K
3 times (Odd/Generic)   Rotary dial (3 states)        Bitwise Column Sum % 3

2 -> 010
2 -> 010
3 -> 011
2 -> 010

Let's count the bits at each position:
* Position 0 (Rightmost bit): 0 + 0 + 1 + 0 = 1  -> 1 % 3 = 1
* Position 1 (Middle bit): 1 + 1 + 1 + 1 = 4 -> 4 % 3 = 1
* Position 2 (Leftmost bit): 0 + 0 + 0 + 0 = 0 -> 0 % 3 = 0
Reconstructing the bits from our modulo results gives us 011, which is 3.

"""


def single_number(nums: list[int]) -> int:
    result = 0

    # Iterate through all 32 possible bit positions
    for i in range(32):
        bit_sum = 0
        for num in nums:
            # Extract the i-th bit of num and add it to the bit_sum
            bit_sum += (num >> i) & 1

        # The bit of the single number is bit_sum % 3
        actual_bit = bit_sum % 3

        # If the bit is 1, set it in our result
        if actual_bit:
            result |= (actual_bit << i)

    # Handle Python's arbitrary-precision integers for negative numbers
    # If the 32nd bit (sign bit) is set, convert it to a 32-bit signed integer
    if result >= 2 ** 31:
        result -= 2 ** 32

    return result

if __name__ == "__main__":
    assert single_number([2,2,3,2]) == 3
    assert single_number([0,1,0,1,0,1,99]) == 99
