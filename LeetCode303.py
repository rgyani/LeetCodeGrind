"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


 Intution: could do for loops for each sum range
 or store a running sum at each pos and then return right - left
-2 -2 1 -4 -2 -3

"""
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # Create a prefix array with an extra 0 at the beginning
        # prefix[i] will store the sum of nums[0] wrapped up to nums[i-1]
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Because of the padding, it's always right+1 minus left
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    assert obj.sumRange(0, 2) == 1
    assert obj.sumRange(2, 5) == -1
    assert obj.sumRange(0, 5) == -3
