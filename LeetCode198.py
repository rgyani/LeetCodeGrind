"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Intution: Nope u cant rob alternate houses, cause the provided inputs are tricky, and u can give suboptimal solution
Consider: [2, 1, 1, 2] -> alternate house give u 3, but u can get 4
Instead, at each house u need to ask if u shud rob this or skip this, that is simply determined by max(amt[i-1], amt[i-2] + amt[i])
"""

def rob(nums: list[int])-> int:
    if not nums:
        return 0

    # 'n_minus_2' represents dp[i-2], 'n_minus_1' represents dp[i-1]
    n_minus_2 = 0
    n_minus_1 = 0

    for num in nums:
        # Calculate the max for the current house
        current = max(n_minus_2 + num, n_minus_1)

        # move the sliding window
        n_minus_2 = n_minus_1
        n_minus_1 = current

    return n_minus_1

if __name__ == "__main__":
    assert rob([1,2,3,1]) == 4
    assert rob([2,7,9,3,1]) == 12
    assert rob([2,9,7,3,1]) == 12
    assert rob([2,9,7,3,9]) == 18
    assert rob([2, 1, 1, 2]) == 4
