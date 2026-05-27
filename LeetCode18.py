"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Intuition: using 4 loops is gonna be O(n^4)
Instead, lets sort the array, and use two loops, where j + i+1, left = j+1, right = len(nums) -1
Then at each step, we check if sum = nums[i] + nums[j] + nums[left] + nums[right] == target
and move pointers, left++, right-- if sum == target
if sum > target, we need a smaller number, so right--
if sum < target, we need a larger number, so left++
"""


def four_sums(nums:list[int], target:int)-> list[list[int]]:
    nums.sort()
    result = []
    n=len(nums)

    for i in range(n-1):
        # skip duplicate for the first element
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # here we can already optimize if sum(i,i+1, i+2, i+3) > target, we skip this i
        # and also, if sum(i, n-3, n-2, n-1) < target, we skip this i

        for j in range(i+1, n-2):
            # skip duplicate for the second element
            if j > i+1 and nums[j] == nums[j - 1]:
                continue

            # same optimization above can be applied here

            # two pointer approach for the remaining elements

            left, right = j+1, n -1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i],nums[j],nums[left],nums[right]])
                    left +=1
                    right -=1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result

if __name__ == "__main__":
    assert four_sums(nums = [1,0,-1,0,-2,2], target = 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    assert four_sums(nums = [2,2,2,2,2], target = 8) == [[2,2,2,2]]
