"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.



Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Intuition: simply maintain two arrays one for left sum, one for right sum,
and then iterate over it once more if left_sum==right_sum at this inde return it

OR left_sum =0, right_sum = total sum
calculate total sum once, then at each pos, left_sum += current val, right_sum -= current_val, u r good
"""


def pivot_index(nums: list[int]) -> int:
    left_sum = 0
    right_sum = sum(nums)

    for i, val in enumerate(nums):
        right_sum -= val
        # left sum does not include this index
        if left_sum == right_sum:
            return i
        left_sum += val
    return -1


if __name__ == "__main__":
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
    assert pivot_index([1, 2, 3]) == -1
    assert pivot_index([2, 1, -1]) == 0
    assert pivot_index([0, -1, 1, -2, 2]) == 0
    assert pivot_index([-1, 2, 1, 1]) == 2
