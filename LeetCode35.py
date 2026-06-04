"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Intution: binary search, but we keep searching event if l <=r, so that we eventually exhause
1 3 5 6, 7
l=0, r 3, c = 1, s[c] < target
l=2, r 3, c = 2, s[c] < target
l=3  r 3, c = 3, s[c] < target
l=4, r 3, break

1 3 5 6, 2
l=0 r 3 c = 1 s[c] > target
l=0 r=0 c = 0 s[c] < target
l=1 r=0 break

1 3 5 6, 0
l=0 r 3 c = 1 s[c] > target
l=0 r=0 c = 0 s[c] > target
l=0 r=-1 break
"""

def search_insert(nums:list[int], target:int) -> int:
    if not nums:
        return -1

    l,r, m = 0, len(nums)-1, -1
    while l <= r:
        m = l + (r - l)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return r + 1

if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([1, 3, 5, 6], 5) == 2




