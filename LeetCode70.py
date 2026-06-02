"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Intuition: for each step we could be on the n-1 step or n-2 step, so this is classic DP problem
number of ways to reach current step = number of ways to reach current-1 step + number of ways to reach current-2 step

now if current step = 1, there is only 1 way to reach it. climbing 1 step
if current step = 2, there are 2 ways to reach it, directly climbing 2 steps, or first climbing step 1 and then take one more step, so 2
if current step = 3, we can not reach it directly, we always have to reach step 2 or step 1 first, so num of ways = num of ways to reach step1 + num of ways to reach step 2
if current step = 4, we can not reach it directly, we always have to reach step 2 or step 3 first, so num of ways = num of ways to reach step3 + num of ways to reach step 3
"""

def get_steps(n:int)-> int :
    num_steps = [0, 1, 2]

    for i in range (3, n+1):
        num_steps.append(num_steps[i-1] + num_steps[i-2])

    return num_steps[n]

if __name__ == "__main__":
    assert get_steps(1) == 1
    assert get_steps(2) == 2
    assert get_steps(3) == 3
    assert get_steps(4) == 5
    assert get_steps(5) == 8
    assert get_steps(6) == 13
