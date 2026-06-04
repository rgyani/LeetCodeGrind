"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.


Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Intuition:
element can be considered peak if s[i] > s[i-1] and s[i] > s[i+1]

1 2 1 3 | 5 6 4  here 3 > 1 but 3< 5, so its not a peak, so we take the right sub array and continue since the element to the right definately has a peak when compared to current mid

boundary conditions,
1. array is strictly increasing 0 1 2 -> 2 is a peak,
2. array is strictly decreasing 2 1 0 -> 2 is a peak,

"""
from math import inf


def find_peak(nums:list[int]) -> int:
    if len(nums) <= 1:
        return 0

    l, r = 0, len(nums)-1
    while l < r:
        m = l + (r-l)//2
        if nums[m] > nums[m+1] and (nums[m] > nums[m-1] or m == 0):
            return m
        if m != 0 and nums[m -1] > nums[m]:
            r = m
        else:
            l = m + 1

    return l

if __name__ == "__main__":
    assert find_peak([1, 2]) == 1
    assert find_peak([2, 1]) == 0
    assert find_peak([0,1,2]) == 2
    assert find_peak([1,2,3,1]) == 2
    assert find_peak([1,2,1,3,5,6,4]) == 5
    assert find_peak([2, 1, 0]) == 0



