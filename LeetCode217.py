"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Intution: multiple approaches
1. can just count the len of set and len of list
2. can just add numbers one by one to a set, if already exists return false <-- faster
"""

def contains_duplicate(nums:list[int])-> bool:
    # return len(nums) != len(set(nums))

    unique = set()
    for num in nums:
        if num in unique:
            return True
        unique.add(num)
    return False

if __name__ == "__main__":
    assert contains_duplicate([1,2,3,1]) == True
    assert contains_duplicate([1,2,3,4]) == False
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True