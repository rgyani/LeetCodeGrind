"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.



Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

Intution: No intution, but we can solve it like leetcode 1011, where
l = max(nums), r = sum(nums) and we check if m allows us to create the required subarrays

Makes sense since, at worst we have the highest num in the array only,
and at best, we have all the numbers in the array
"""

def split_array(nums:list[int], k :int) -> int:
    def feasible(threshold):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > threshold:
                count += 1
                total = num
                if count > k:
                    return False
        return True

    l, r = max(nums), sum(nums)
    while l< r:
        m = l + (r - l)//2
        if feasible(m):
            r = m
        else:
            l = m + 1

    return l

if __name__ == "__main__":
    assert split_array(nums = [7,2,5,10,8], k = 2) ==18
    assert split_array(nums = [1,2,3,4,5], k = 2) == 9