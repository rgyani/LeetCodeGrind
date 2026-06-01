"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.


Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Intuition: Since this is a binary array this should require a simpler implementation of LeetCode #560

Since there can be no negatives in binary,
[1,0,1,0,1], we keep a counter to store the running sum seen at each pos

create a running sum array
0, 1, 1, 2, 2 3

then we use two pointers, left=0, right=0 and keeps moving to the right till we reach goal, at this point,
we keep increment left till running_sum[right] - running_sum[left] <= goal

this is O(N^2)

this running sum can instead be stored in a map
{0:1, 1:2, 2: 2, 3: 1}
and then we check if goal - this key, exists in our map and sum the count
Since this is binary, it can only increase decrease by one, so we are good covering the whole range
"""
from collections import defaultdict


def num_subarrays_with_sum(nums: list[int], goal: int) -> int:
    running_sum = 0

    map_counts = defaultdict(int)
    map_counts[0] = 1

    counts = 0
    for num in nums:
        running_sum += num

        if running_sum - goal in map_counts:
            counts += map_counts[running_sum - goal]

        map_counts[running_sum] +=1

    return counts

if __name__ == "__main__":
    assert num_subarrays_with_sum(nums=[1, 0, 1, 0, 1], goal=2) == 4
    assert num_subarrays_with_sum(nums=[1, 0, 1, 0, 1], goal=1) == 8
    assert num_subarrays_with_sum(nums=[0, 0, 0, 0, 0], goal=0) == 15
