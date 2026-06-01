"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Intuition:

Also consider
[1, -1, 2, -3, 2, 3], k = 1 ->  [1], [-1,2], [2,-3,2], [1,-1,2,-3,2]

since the array is not sorted and can contain negatives, naive approach is to choose this element, and scan both left and right till u get the sum
remember it is a contiguous array, u need to include all elements

what if we get running_sum
[1, 0, 2, -1, 1, 4]

so now at each position as u iterate over this running_sum_array u just need to check if u have seen val[i] - k
so the solution simply becomes, track a current_sum, store it at index, if current_sum-k is in the map, u increment your counter

Basically, as I walk forward, how many times have I already seen the value (current_sum - k)?
"""


def subarray_sum(nums: list[int], k: int) -> int:
    # running sum, how many times we have seen it
    sum_frequencies = {0:1} # handles remaining = 0 without extra if
    counter = 0
    running_sum = 0

    for i, num in enumerate(nums):
        running_sum += num
        remaining = running_sum - k

        # have i seen this value? yes, we found a sub array
        counter += sum_frequencies.get(remaining, 0)
        sum_frequencies[running_sum] = sum_frequencies.get(running_sum, 0) + 1
    return counter

if __name__ == "__main__":
    assert subarray_sum(nums = [1,1,1], k = 2) == 2
    assert subarray_sum([1,2,3], k = 3) ==2
    assert subarray_sum([1, -1, 2, -3, 2, 3], k = 1) == 4
    assert subarray_sum([1], k = 0) == 0
    assert subarray_sum(nums = [1,1,1], k = 1) == 3
    assert subarray_sum([0,0,0], k = 0) == 6
    assert subarray_sum([0,0,0,0,0,0,0,0,0,0], k = 0) == 55