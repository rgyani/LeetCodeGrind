"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Intution: At first glance it looks like we can loop over 1..n, where n=max(piles) and check if eating i bananas per hour satisfies our condition
what we are doing here is finding the max i [1, max(piles)] which satisfies the condition that with this speed, all bananaas are finished in h hours
so this becomes a binary search (O(logN)) where we check the mid with a function

"""

def min_eating_speed(piles:list[int], h:int)->int:
    def is_feasible(speed:int):
        # each pile is eaten with 'speed' then total hours shud be less than 'h'
        time_taken = 0
        for pile in piles:
            time_taken += pile // speed + (0 if pile%speed == 0 else 1)
        return time_taken <= h


    l,r = 1, max(piles)
    while l < r:
        m = l + (r - l) //2
        if is_feasible(m):
            r = m
        else:
            l = m+1
    return l


if __name__ == "__main__":
    assert min_eating_speed( piles = [3,6,7,11], h = 8) == 4
    assert min_eating_speed(piles = [30,11,23,4,20], h = 5) ==30
    assert min_eating_speed(piles = [30,11,23,4,20], h = 6) == 23