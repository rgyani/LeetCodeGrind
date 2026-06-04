"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Input: nums = [1,1,1,1,1,1], target = 1
output = [0, 7]

Intution: Binary search to find the element, since it is sorted already,
once found, u again move left and right using binary search
"""
from math import inf


def search_range(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]

    def find(look_left:bool):
        l, r = 0, len(nums)-1
        bound = -1
        while l <= r:
            m = (l + r) //2

            if nums[m] == target:
                bound = m
                if look_left:
                    # Look left to find an even earlier occurrence
                    r = m -1
                else:
                    # Look right to find an even later occurrence
                    l = m + 1
            elif nums[m] < target:
                l += 1
            else:
                r = m-1
        return bound

    return [find(True), find(False)]

if __name__ == "__main__":
    assert search_range(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert search_range(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    assert search_range(nums=[], target=0) == [-1, -1]
    assert search_range(nums=[1,1,1,1,1,1,1], target=1) == [0, 6]
