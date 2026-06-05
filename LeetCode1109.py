"""
There are n flights that are labeled from 1 to n.

You are given an array of flight bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.


Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]

Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

Example 2:

Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25

Hence, answer = [10,25]

Intution: looks simple right, find min and max, create an array for these, then iterate thru the list, for min to max, update the sum
"""
from math import inf


def flights(bookings:list[list[int]], n:int) -> list[int]:
    op = [0] * n

    for l, r, seats in bookings:
        op[l - 1] += seats
        if r < n:
            op[r] -= seats

    for i in range(1, n):
        op[i] += op[i - 1]

    return op

if __name__ == "__main__":
    assert flights([[1,2,10],[2,3,20],[2,5,25]], n = 5) == [10,55,45,25,25]
    assert flights(bookings = [[1,2,10],[2,2,15]], n = 2) == [10,25]