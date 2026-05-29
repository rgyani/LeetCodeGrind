"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


#Intuition: Classic 3Sum problem, brute force approach is to take three nested loop O(n^3)
Instead, lets sort the array and use 2 pointers, loop thru till u get num[i] > 0, since other elements will be greater
then left = i+1, right = len-1, if sum[i] + sum[left] + sum[right] == 0, we found a valid triplet
else if sum < 0, we need a larger number, so left++,
else if sum > 0, we need a smaller number, so right--

"""

def three_sum(nums: list[int]) -> list[list[int]]:
    results = []

    nums.sort()

    for i in range(len(nums)):
        # other elements to the right will be greater, no way sum can be 0
        if nums[i] > 0:
            break

        # same element we checked last time, can skip it safely
        if i > 0 and nums[i-1] == nums[i]:
            continue

        left, right = i + 1, len(nums) -1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                results.append([nums[i], nums[left], nums[right]])

                # Move pointers and skip duplicates
                left += 1
                right -= 1

                # but the elements might repeat, so keep moving if u get similar elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1 # Need a larger value
            else:
                right -= 1 # Need a smaller value

    return results

if __name__ == "__main__":
    assert three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert three_sum([0,1,1]) == []
    assert three_sum([0,0,0]) == [[0,0,0]]
    assert three_sum([1,2,0,1,0,0,0,0]) == [[0,0,0]]