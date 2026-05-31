"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]


Intution: for 2 strings to be anagrams, their sorted values must be equal
so we run thru the list, sort each string and store them in map, then iterate and return the values
"""
from collections import defaultdict


def group_anagrams(strs:list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)

    for s in strs:
        k = "".join(sorted(s))
        anagram_map[k].append(s)

    return list(anagram_map.values())

if __name__ == "__main__":
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]