"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Intuiton: Since the list is already sorted, we can keep two pointers left = 0 and right=len(numbers) -1
if sum of numbers[left] + numbers[right] == 9, return
else if sum > target, we do right--,
else if sum < target, we do left++
"""

def two_sum(numbers:list[int], target:int) -> list[int]:
    if not numbers:
        return []

    left,right = 0, len(numbers) -1

    while left< right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

if __name__ == "__main__":
    assert two_sum(numbers = [2,7,11,15], target = 9) == [1,2]
    assert two_sum(numbers = [2,3,4], target = 6) == [1,3]
    assert two_sum(numbers = [-1,0], target = -1) == [1,2]