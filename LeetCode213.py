"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


# Intuition: This is similar to LeetCode198.py, just now we cant choose first and last house
So Instead we split the list into two parts, 0 to n-1 and 1 to n
"""

def rob_subset(nums: list[int])-> int:
    # n_minus_2 represents dp[i-2], n_minus_1 represents dp[i-1]
    n_minus_2 = 0
    n_minus_1 = 0

    for num in nums:
        # Calculate the max for the current house
        current = max(n_minus_2 + num, n_minus_1)

        # move the sliding window
        n_minus_2 = n_minus_1
        n_minus_1 = current

    return n_minus_1

def rob(nums:list[int])->int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    return max(rob_subset(nums[:-1]), rob_subset(nums[1:]))

if __name__ == "__main__":
    assert rob([2,3,2]) == 3
    assert rob([1,2,3,1]) == 4
    assert rob([1,2,3]) == 3