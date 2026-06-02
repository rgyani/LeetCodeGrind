"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Intuition:
Keep expanding the window, till u reach or exceed the desired sum -> note min_length
Once reached, keep shrinking the window from left till below desired sum -> note min_length
Now continue expanding the window again
"""

from math import inf
from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    if not nums:
        return 0

    left = 0
    sum = 0

    length = inf
    # iterate thru the array, adding item to the sum
    for right, val in enumerate(nums):
        sum += val

        # as soon as we hit the target, we start removing elements from the left
        while sum >= target:
            # note current length
            length = min(length, right - left + 1)
            sum -= nums[left]
            left += 1

    return 0 if length == inf else int(length)

if __name__ == "__main__":
    assert min_sub_array_len(7, [2,3,1,2,4,3]) == 2
    assert min_sub_array_len(4, [1,4,4]) == 1
    assert min_sub_array_len(11, [1,1,1,1,1,1,1,1]) == 0
