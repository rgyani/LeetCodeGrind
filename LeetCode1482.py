"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.



Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

Example 3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.


Intuition:
for [1,10,3,10,2], m = 3, k = 1 on day 3, we have
T F T F T, since k = 1, we can pick each flower

Intuition: what if we use the l = min(days), r=max(days) and see if we can create bouquets
This is is a binary search, where at each m we check if creating boquets is possible
"""

def check_possible(bloomDay:list[int], m: int, k:int)->int:
    def can_create(days):
        flowers, total = 0, 0
        for bloom in bloomDay:
            if bloom > days: # if we bloom after the given day, we cant use this flower
                flowers = 0
            else:
                # flowers keep increasing, check if we have enuf for a bucket
                total +=  (flowers + 1) // k
                # once we have enough, reset the flower count
                flowers= (flowers + 1) %k
        return total >= m

    l = 1
    r = max(bloomDay)

    if not can_create(r):
        return -1

    while l < r:
        middle = l + (r - l)//2
        if can_create(middle):
            r = middle
        else:
            l = middle + 1

    return l

if __name__ == "__main__":
    assert check_possible([1,10,3,10,2], m = 3, k = 1) == 3
    assert check_possible([1,10,3,10,2], m = 3, k = 2) == -1
    assert check_possible([7,7,7,7,12,7,7], m = 2, k = 3 ) == 12
