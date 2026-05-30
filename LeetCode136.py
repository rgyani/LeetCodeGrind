"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3
Input: nums = [1]
Output: 1

Intuition: Remember
A XOR 0 = A
A XOR A = 0

so if a number appears twice, it will be reduced to 0,
"""

def single_number(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    assert single_number([2, 2, 1]) == 1
    assert single_number([4,1,2,1,2]) == 4
    assert single_number([1]) == 1
