"""
Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ...
where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).

For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happen before addition and subtraction.
It is not allowed to use the unary negation operator (-). For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
We would like to write an expression with the least number of operators such that the expression equals the given target. Return the least number of operators used.



Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.
The expression contains 5 operations.

Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
The expression contains 8 operations.

Example 3:

Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.
The expression contains 3 operations.

Intuition:
we are trying to reach a destination (the target) by taking steps.
our only allowed step sizes are powers of x.
If x = 3, our allowed step sizes are:
    * 1 (which we write as 3 / 3)
    * 3 (which we write as 3)
    * 9 (which we write as 3 * 3)
    * 27 (which we write as 3 * 3 * 3)
Every time we choose a step size, we pay a "cost" in operators.
Larger steps actually cost more operators to type out because they require more multiplications.

At any given moment, we look at our target and find the closest giant step size that fits into it.
We always have exactly two choices:
    The Floor (Under-shooting): we tae the largest steps we can without going over, and then figure out how to cover the small remaining distance.
    The Ceiling (Over-shooting): take one extra large step to go past the target, and then figure out how to step backward to correct it.

eg x = 3, target = 19
The closest power of 3 near 19 is 9 (3 * 3). 19 = 9 + 9 + 1
    Choice 1: The Floor (Stop at 18) We take two steps of 3 * 3 + 3 * 3, then add the remaining target which is 1 = 3/3 -> Total ops = 5
    Chouce 2: The Ceiling (Overshoot to 27) Instead of stopping at two 9s, we take three 9s: 3*3+ 3*3 + 3*3 and subtract 8. To get 8 we need 1 + whatever ops 8 requires, but we already are at 6 ops,

So we can either do it via DP or just making the choice 1 or choice 2 based on info so far using a graph to represent the hightest power seen so far and finding the short path from target to 0
so
19 = 6 X 3 + 1  we solve for both 6 and 1 now, knowing we need one more operation to join them
19  = 7 * 3 - 2, we solve for both 7 and 2 now, knowing we need one more operation to join them

"""


def least_ops_express_target(x: int, target: int) -> int:
    remainder = target % x

    # floor: cost to make remainder units
    floor = remainder * 2
    # ceil: cost to overshoot to the next multiple of x
    ceil = (x - remainder) * 2

    # Move to power = 1 (the x place, e.g., 3)
    target //= x
    power = 1

    while target > 0:
        remainder = target % x

        # A block at the current power costs exactly 'power' operations.
        # Example: if power=1 (3s place), a 3 costs 1 op (the connecting sign)
        # If power=2 (9s place), a 3*3 costs 2 ops (1 multiplication + 1 connecting sign)

        # To find the new floor:
        # 1. Stayed on floor path: add 'remainder' blocks of current power
        # 2. Came from ceil path: we overshot last time, so we have 1 extra block.
        #    We only need remainder + 1 blocks.
        next_floor = min(remainder * power + floor, (remainder + 1) * power + ceil)

        # To find the new ceil:
        # 1. Coming from floor path: we need x - remainder blocks to overshoot
        # 2. Coming from ceil path: we already have 1 extra block, so we only need x - remainder - 1 blocks
        next_ceil = min((x - remainder) * power + floor, (x - remainder - 1) * power + ceil)

        floor = next_floor
        ceil = next_ceil

        target //= x
        power += 1

    # Finally, the result is the minimum of:
    # 1. The floor path
    # 2. The ceil path + the cost of the final carried-over power block
    # We subtract 1 because the very first term doesn't need a leading '+' or '-' sign.
    return min(floor, ceil + power) - 1

if __name__ == "__main__":
    assert least_ops_express_target(x=3, target=19) == 5
    assert least_ops_express_target(x=5, target=501) == 8
    assert least_ops_express_target(x=100, target=100000000) == 3
    assert least_ops_express_target(x=3, target=1) == 1
    assert least_ops_express_target(x=3, target=2) == 2
    assert least_ops_express_target(x=3, target=3) == 0
    print("All tests passed successfully!")


