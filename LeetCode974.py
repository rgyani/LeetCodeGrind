"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0



Intuition: keep a running sum in a counter, if running_sum % k in the map, count += value
 """
from collections import Counter, defaultdict


def sub_array_div_by_k(nums:list[int], k:int)->int:
    running_sum = 0
    counter = defaultdict(int)

    counter[0] = 1

    counts = 0
    for num in nums:
        running_sum += num

        remainder = running_sum % k
        counts += counter[remainder]
        counter[remainder] += 1

    return counts

if __name__ == "__main__":
    assert sub_array_div_by_k(nums = [4,5,0,-2,-3,1], k = 5) == 7
    assert sub_array_div_by_k(nums = [5], k = 9) == 0
