"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.


Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.


Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false


Intuition:
if prefix_sum(j) - prefix_sum(i) % k == 0 and j-i >=2 we have a solution

so we keep tracking prefix_sum % k : first seen in a map
for each element if we get prefix_sum % k in this map, we check current index - index from map, it this is >=2 we return True
"""


def check_sub_arraySum(nums: list[int], k: int) -> bool:
    # Map to store the first occurrence of a remainder: {remainder: index}
    # We initialize 0 with -1 to handle valid subarrays starting at index 0.
    remainder_map = {0: -1}
    running_sum = 0

    for i, num in enumerate(nums):
        running_sum += num
        rem = running_sum % k

        if rem in remainder_map:
            # Check if the subarray length is at least 2
            if i - remainder_map[rem] >= 2:
                return True
        else:
            # Only store the first occurrence to maintain the longest possible distance
            remainder_map[rem] = i

    return False


if __name__ == "__main__":
    assert check_sub_arraySum(nums=[6, 1, 1, 1, 1, 1], k=6) == False
    assert check_sub_arraySum(nums=[23, 2, 4, 6, 7], k=6) == True
    assert check_sub_arraySum(nums=[23, 2, 6, 4, 7], k=6) == True
    assert check_sub_arraySum(nums=[23, 2, 6, 4, 7], k=13) == False
    assert check_sub_arraySum(nums=[23, 2, 6, 4, 7], k=1) == True
    assert check_sub_arraySum(nums=[1, 1, 1, 1, 1, 1], k=6) == True
    assert check_sub_arraySum(nums=[5, 0, 0, 0], k=3) == True
    assert check_sub_arraySum(nums=[5, 0, 0, 0], k=3) == True
    assert check_sub_arraySum(nums=[0, 2, 5, 6, 1], k=6) == True
