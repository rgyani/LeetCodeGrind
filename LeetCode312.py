"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10


Intution: build a DP array to find out the max value
where dp[i][j] means the baloons between i and j are burst
For dp[i][j], we tries every balloon k between i and j as the last one burst. The formula is:
nums[i] * nums[k] * nums[j]   ← coins for bursting k last
+ dp[i][k]                    ← best coins left of k
+ dp[k][j]                    ← best coins right of k

  1  3  1  5  8  1
  0  1  2  3  4  5           <- j
0       3                    <- baloons between 0 and 2 is burst-
1          15                <- baloons between 1 and 3 is burst
2              40
3                 40
4
5

for gap 2
    dp[0][2] : last balloon burst between indices 0 and 2:
        k=1 (nums[1]=3)	1×3×1 + dp[0][1] + dp[1][2]	 = 3

    dp[1][3] : last balloon burst between indices 1 and 3:
        k=2 (nums[2]=1)	3×1×5 + dp[1][2] + dp[2][3]	 = 15

    dp[2][4] : last balloon burst between indices 2 and 4:
        k=3 (nums[3]=5)	1×5×8 + dp[2][3] + dp[3][4]	 = 40

now gap is 3,
    dp[0][3] : last balloon burst between indices 0 and 3:
        k=1 (nums[1]=3)	1×3×5 + dp[0][1] + dp[1][3]	= 30
        k=2 (nums[2]=1)	1×1×5 + dp[0][2] + dp[2][3]	 = 8

    dp[1][4] : last balloon burst between indices 1 and 4:
        k=2 (nums[2]=1)	3×1×8 + dp[1][2] + dp[2][4]	= 64
        k=3 (nums[3]=5)	3×5×8 + dp[1][3] + dp[3][4]	= 135

    dp[2][5] : last balloon burst between indices 2 and 5:
        k=3 (nums[3]=5)	1×5×1 + dp[2][3] + dp[3][5]	= 45
        k=4 (nums[4]=8)	1×8×1 + dp[2][4] + dp[4][5]	= 48

"""


def max_coins(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # iterate over all window sizes (gap between left and right)
    for gap in range(2, n):  # gap=2 means one balloon between
        for left in range(n - gap):
            right = left + gap
            for k in range(left + 1, right):  # k is last burst
                coins = nums[left] * nums[k] * nums[right]
                dp[left][right] = max(
                    dp[left][right],
                    coins + dp[left][k] + dp[k][right]
                )

    return dp[0][n - 1]

if __name__ == "__main__":
    assert max_coins([3,1,5,8]) == 167
    assert max_coins([1,5]) == 10