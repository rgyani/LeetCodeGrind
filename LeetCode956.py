"""
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.



Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.


Intution:
each rod can be placed in one of three states—left support, right support, or left out entirely—
a brute-force approach would take O(n^3) time, which is too slow for larger sets.

d = left_height - right_height

"""


def tallestBillboard(rods: list[int]) -> int:
    # dp[diff] = max height of the shorter support with that difference
    dp = {0: 0}

    for r in rods:
        # We must copy the current DP state so updates from this rod
        # don't interfere with other choices for the same rod
        current_dp = dp.copy()

        for d, h in current_dp.items():
            # Choice 1: Put rod on the taller side
            # New difference increases by r, short side height stays 'h'
            dp[d + r] = max(dp.get(d + r, 0), h)

            # Choice 2: Put rod on the shorter side
            # New difference is the absolute difference, short side grows by min(d, r)
            new_d = abs(d - r)
            new_h = h + min(d, r)
            dp[new_d] = max(dp.get(new_d, 0), new_h)

    # The answer is the max height of the shorter side when the difference is 0
    return dp.get(0, 0)

if __name__ == "__main__":
    assert tallestBillboard([1,2,3,6]) == 6
    assert tallestBillboard([1, 2]) == 0
    assert tallestBillboard([1, 2, 3, 4, 5, 6]) == 10

