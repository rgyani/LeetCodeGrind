"""
Given an integer array nums of length n and an integer target,
find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Intuition:
using 3 loops is gonna be O(n^3)
Instead, we sort the array, fix i, then left = i+1, right = len-1
and now we track the closest_sum at each step and return that
if closest_sum == target, we return immediately
else if current_sum < target, we need a bigger number, so left++
else if current_sum > target, we need a smaller number, so right--
"""


def three_sum_closest(nums: list[int], target: int) -> int:
    nums.sort()  # Sort the array
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        # Skip duplicate fixed elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # If we found the exact target, return immediately, what could be better
            if current_sum == target:
                return current_sum

            # Update the closest sum if the current one is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move pointers based on how the current sum compares to the target
            if current_sum < target:
                left += 1  # We need a larger sum
            else:
                right -= 1  # We need a smaller sum

    return int(closest_sum)

if __name__ == "__main__":
    assert three_sum_closest([-1,2,1,-4], 1) == 2
    assert three_sum_closest([0,0,0], 1) == 0