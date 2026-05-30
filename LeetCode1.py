"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Intuition: iterate over list, store in a map, the number and its index, also calculate the complement = target-num
as we are doing this, if we already have the complement in the map, we return this and the complement's index
"""

def two_sum(nums:list[int], target:int)-> list[int]:
    # Stores { number_seen: its_index }
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        # If the complement is already in our map, we found the pair!
        if complement in seen:
            return [seen[complement], i]

        # else srore it
        seen[num] = i

    return [-1,-1]

if __name__ == "__main__":
    assert two_sum(nums = [2,7,11,15], target = 9) == [0,1]
    assert two_sum(nums = [3,2,4], target = 6) == [1,2]
    assert two_sum(nums = [3,3], target = 6) == [0,1]