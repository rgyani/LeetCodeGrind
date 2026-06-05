"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.



Example 1:Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Intution: first run thru the list, find min start, max end, then iterate thru these ranges
at each point
if first item is equal to i, we add to capacity
if second items is equal to i, we decrease capacity,
if at any point capacity > max_capacity we return false
"""
from math import inf


def car_pooling(trips:list[list[int]], capacity:int)->bool:
    current_cap = 0
    i, j = inf, 0
    for trip in trips:
        i = min(i, trip[1])
        j = max(j, trip[2])

    for k in range(i, j+1):
        for trip in trips:
            if trip[1] == k:
                current_cap += trip[0]
            if trip[2] == k:
                current_cap -= trip[0]

        if current_cap > capacity:
            return False

    return True

if __name__== "__main__":
    assert car_pooling(trips = [[2,1,5],[3,3,7]], capacity = 4) == False
    assert car_pooling(trips = [[2,1,5],[3,3,7]], capacity = 5) == True
    assert car_pooling([[2,1,5],[3,5,7]], 3) == True
    assert car_pooling([[4,5,6],[6,4,7],[4,3,5],[2,3,5]], 13) == True