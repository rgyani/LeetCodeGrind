"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Intution: Read LeetCode191.py
we can loop from 0 to n inclusive and calculate hamming weight of each number
but remember bits in i are just bits in i//2 moved to the left, plus 1 if i is odd
"""

def count_bits(n:int)->list[int]:
    ans = [0] * (n+1)

    for i in range(1, n+1):
        ans[i] = ans[i//2] + (1 if i%2 ==1 else 0)

    return ans

if __name__=="__main__":
    assert count_bits(2) == [0,1,1]
    assert count_bits(5) == [0,1,1,2,1,2]
