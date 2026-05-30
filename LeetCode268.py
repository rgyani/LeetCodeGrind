"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Intuition: I would go with school formula
sum of numbers from 1..N is N * (N+1)/2

iterate thru the list, find min and max, then apply the formula to get missing number

you could also do it with XOR
run thru the list, XOR item with its position, so 3^0 ^ 0^1 ^ 1^2 = 3^3 ^ 2 ^ 1^1 ^ 0^0 = 2
"""

def missing_number(nums:list[int]) -> int:
    l = len(nums)
    sum = l*(l+1)//2

    for i in nums:
        sum -= i

    return sum

if __name__ == "__main__":
    assert missing_number([3,0,1]) == 2
    assert missing_number([0,1]) == 2
    assert missing_number([9,6,4,2,3,5,7,0,1]) == 8


