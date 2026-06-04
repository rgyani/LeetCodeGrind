"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Intution: simple binary search since we need to find the number in a sorted array

target 9
-1 0 3 | 5 9 12
         5 9 | 12

target 2
-1 0 3 | 5 9 12
-1 0 | 3
"""

def search(nums:list[int], target:int)->int:
    l, r = 0, len(nums)-1

    while l <= r:
        m = l + (r - l)//2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1

if __name__ == "__main__":
    assert search(nums = [5], target = 5) == 0
    assert search(nums = [-1,0,3,5,9,12], target = 9) == 4
    assert search(nums = [-1,0,3,5,9,12], target = 2) == -1

