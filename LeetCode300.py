"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Intuition: we can simply use DP and for each position, look at left to find a smaller element and increase the subsequence counter
so dp[i] = max(dp[j], 1)
This is O(n^2) approach


"""


def length_of_longest_increasing_subsequence(nums:list[int]) -> int:
    if not nums:
        return 0

    dp = [1] * len(nums)

    # Check all previous values
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == "__main__":
    assert length_of_longest_increasing_subsequence([10,9,2,5,3,7,101,18]) ==4
    assert length_of_longest_increasing_subsequence([0,1,0,3,2,3]) == 4
    assert length_of_longest_increasing_subsequence([7,7,7,7,7,7,7]) == 1