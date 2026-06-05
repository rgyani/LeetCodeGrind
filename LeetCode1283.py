"""
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor,
divide all the array by it, and sum the division's result.

Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

Example 1:
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).

Example 2:
Input: nums = [44,22,33,11,1], threshold = 5
Output: 44


Intution:
44,22,33,11,1

for divisor 22, we get 2 + 1 + 2 + 1 + 1 = 7
for divisor 44, we get 1 + 1 + 1 + 1 + 1 = 5

so the solution becomes l=1, r=max(nums), find min m where the condition holds true
"""

def smallest_divisor(nums:list[int], threshold:int)->int:
    def condition(m):
        total = sum([num//m + (0 if num%m == 0 else 1) for num in nums])
        return total <= threshold

    l,r = 1, max(nums)
    while l < r:
        m = l + (r -l)//2
        if condition(m):
            r = m
        else:
            l = m + 1

    return l

if __name__ == "__main__":
    assert smallest_divisor(nums = [1,2,5,9], threshold = 6) == 5
    assert smallest_divisor(nums = [44,22,33,11,1], threshold = 5) == 44