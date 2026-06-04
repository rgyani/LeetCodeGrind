"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Intution: do a binary search on the array

3 4 5 | 1 2  or 5 1 2 | 3 4 or 4 5 1 | 2 3 or 1 2 3 | 4 5
       1 | 2    5 1 | 2        4 5 | 1        1 2 | 3
                5 | 1                         1 | 2

if s[l] < s[c], that means it is still perfectly sorted,
    we search in right part now IFF s[r] < s[c]
    else we search in left part only
if s[l] > s[c], that means it contains the rotated 0th element, keep searching here
"""


def find_min(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        c = l + (r - l) // 2
        if nums[l] <= nums[c]:
            if nums[r] < nums[c]:
                l = c + 1
            else:
                r = c
        else:
            r = c

    return nums[l]


if __name__ == "__main__":
    assert find_min([5, 1, 2, 3, 4]) == 1
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 1, 2, 3]) == 1
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([4, 0]) == 0
    assert find_min([11, 13, 15, 17]) == 11
