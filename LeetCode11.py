"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Intuition: Use 2 pointers, left =0 and right = len(height) -1
Calculate max_water = right-left * min(height[left], height[right])
now if height[left] < height[right] -> move left + 1, else move right -1
keep doing this till left < right
"""
from typing import List


def max_area(height:List[int])-> int:
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Calculate the area
        current_width = right - left
        current_height = min(height[left], height[right])
        current_area = current_width * current_height

        # Update the maximum water found so far
        max_water = max(max_water, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert max_area([1,1]) == 1