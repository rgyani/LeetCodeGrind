"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9


Intuition: to trap water at any point, we need a higher left and a higher right wall
So we could brute force this to find the tallest wall to both left and right
This would be O(n^2) approach

What if we scan the list and at each point store the highest wall to the left
Then we REVERSE scan the list again and store the highest wall to the right
So that means we store two arrays for left_max and right_max

This is perfectly valid O(n) solution, but needs storing two extra arrays.
We can do better with a two pointer approach,

where we keep left and right pointers to the highest walls we have seen
Now if we had highest_left < highest_right, we cannot store anything above highest_left since no matter the current wall height, everything will spill over on the left side
Similarly on the right side, and now we can squeeze the two pointers till they meet in the middle
"""


def trap(heights:list[int])-> int:
    if not heights:
        return 0

    water = 0
    left, right = 0, len(heights)-1
    left_max, right_max = heights[left], heights[right]

    while left < right:
        # the smaller wall dictates the water storage
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])

            # Water trapped is the bottleneck minus current height
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])

            water += right_max - heights[right]

    return water

if __name__ == "__main__":
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4, 2, 3]) == 1