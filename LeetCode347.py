"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]


Intution: Simply do,     # counts = Counter(nums)
    return [e for e, v in counts.most_common(k)] # O(logN) since most_common uses a heap internally

"""
from collections import Counter


def top_k_frequent(nums:list[int], k:int)->list[int]:
    counts = Counter(nums)
    return [e for e,v in counts.items() if v >= k]
    return [e for e, v in counts.most_common(k)]


if __name__ == "__main":
    assert sorted(top_k_frequent([1,1,1,2,2,3], 2)) == [1,2]
    assert sorted(top_k_frequent([1], 1)) == [1]
    assert sorted(top_k_frequent( [1,2,1,2,1,2,3,1,3,2], k = 2)) == [1,2]
