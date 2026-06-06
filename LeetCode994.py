"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Intution: Keep a simple set, where u store rotten apples,
iterate on minutes, move new rotten to the set, till u get nothing rotten
"""

def oranges_rotting(grid: list[list[int]]) -> int:
    num_oranges = 0
    rotten = set()

    for i, lst in enumerate(grid):
        for j, state in enumerate(lst):
            if state == 0:
                continue
            num_oranges += 1
            if state == 2:
                rotten.add((i,j))


    minute = -1
    found = True
    while found:
        found = False
        rotten_now = set()
        minute += 1
        for i, lst in enumerate(grid):
            for j, state in enumerate(lst):
                if state == 0:
                    continue
                if (i,j) in rotten:
                    continue
                if (i-1, j) in rotten or \
                        (i+1,j) in rotten or \
                        (i, j-1) in rotten or \
                        (i, j+1) in rotten:
                    rotten_now.add((i,j))
                    found = True
        rotten |= rotten_now

    return minute if len(rotten) == num_oranges else -1

if __name__ == "__main__":
    assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) ==4
    assert oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert oranges_rotting([[0,2]]) == 0