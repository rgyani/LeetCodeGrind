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

Intuition: say if we had x=10, target = 19, with base 10, we would have compared minops( 2 * 10^1 - 1*10^0, 1 * 10^1 + 9 * 10^0)
but now we have x=3 so 19base3 is
19/3 = 6 with remainder 1
6/3  = 2 with remainder 0
2/3 =  0 with remainder 2
the 19base3 hence is 201

so we compare 2 * 3^2 + 0 * 3^1 + 1 * 3^0 with


501base5 was 4001, so we have minops(4 * 5^3 + 0 * 5^2 + 0 * 5^1 + 1 * 5^0, 1 * 5^4 - 1 * 5^3 + 1 * 5^0)

so there is no intution, we just need to understand this and then simple compare
"""

def least_ops_express_target(x:int, target:int) -> int:
    memo = {}

    def dfs(target: int) -> int:
        # Base case: if target is less than x, we evaluate it directly
        if target < x:
            # e.g., if x=3, target=2: we can do '3/3 + 3/3' (4 ops)
            # or '3 - 3/3' (2 ops). We choose the minimum.
            return min(2 * target - 1, 2 * (x - target))

        if target in memo:
            return memo[target]

        # Find the power of x just below or equal to target
        product = x
        times = 1
        while product * x <= target:
            product *= x
            times += 1

        # exact match
        if product == target:
            return times - 1

        # Option 1: Keep the current chunk and recurse on the remainder
        # Example: 11 // 9 = 1 chunk of 9, remainder 2
        # Cost is (times * count) + cost of remainder
        count = target // product
        rem1 = target - product * count
        ans = count * times + dfs(rem1)

        # Option 2: Round up to the next multiple and subtract the difference
        # Example: Round up to 2 chunks of 9 (18), remainder 7
        rem2 = product * (count + 1) - target
        if rem2 < target:  # Avoid infinite loops
            ans = min(ans, (count + 1) * times + dfs(rem2))

        memo[target] = ans
        return ans

    return dfs(target)

if __name__ == "__main__":
    assert least_ops_express_target(x=3, target=19) == 5
    assert least_ops_express_target(x=5, target=501) == 8
    assert least_ops_express_target(x=100, target=100000000) == 3
    assert least_ops_express_target(x=3, target=1) == 1
    assert least_ops_express_target(x=3, target=2) == 2
    assert least_ops_express_target(x=3, target=3) == 0


