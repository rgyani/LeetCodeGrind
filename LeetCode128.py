"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Intituion: make as hashset containing each element, then run thru the hashset, to find if i-1 exists in the set
if it doesnot, then this could be the start of a seq, then keep checking for i+1, i+2 and so on, note max found so far
"""


def longest_consecutive(nums: list[int]) -> int:
    hash_set = set(nums)

    max_val = 0
    for num in hash_set:
        if num -1 not in hash_set: # this is the start of a sequence
            counts = 0
            i = num
            while i in hash_set:
                counts += 1
                max_val = max(max_val, counts)
                i += 1

    return max_val

if __name__ == "__main__":
    assert longest_consecutive([100,4,200,1,3,2]) == 4
    assert longest_consecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert  longest_consecutive([1,0,1,2]) == 3
    assert longest_consecutive([]) == 0
    assert longest_consecutive([-101,-102, -103, -104,-200,1,3,2]) == 4
