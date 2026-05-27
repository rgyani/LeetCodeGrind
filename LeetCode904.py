"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.



Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


Intuition:
Remember, if u start picking from a tree, u need to pick from next tree no matter what
So we scan thru the tree from left to right, add the fruit to the basket -> note the max_fruits
If the length of basket > 2, we keep dropping the left most fruit till length of basket is 2 again -> note max_fruits again
"""

from typing import List


def total_fruits(fruits: List[int]) -> int:
    if not fruits:
        return 0

    baskets = {}
    left = 0
    max_fruits = 0

    # just scan thru the list
    for right, fruit in enumerate(fruits):
        # add fruit to the bucket
        baskets[fruit] = baskets.get(fruit, 0) + 1

        # if we got more than 2 fruits in our bucket
        while len(baskets) > 2:
            # keep shifting left
            baskets[fruits[left]] -= 1
            if baskets[fruits[left]] == 0:
                del baskets[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


if __name__ == "__main__":
    assert total_fruits([1, 2, 1]) == 3
    assert total_fruits([0, 1, 2, 2]) == 3
    assert total_fruits([1, 2, 3, 2, 2]) == 4
    assert total_fruits([1, 2, 3, 1, 2]) == 2
    assert total_fruits([1, 1, 2, 3, 1, 3, 3, 3]) == 5
