"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Intution: hashmap containing counters of the two string, if they are equal, return true
"""
from collections import Counter


def is_anagram(s:str, t:str)->bool:
    s_counter = Counter(s)
    t_counter = Counter(t)

    return s_counter == t_counter

if __name__ == "__main__":
    assert is_anagram("anagram", t = "nagaram") == True
    assert is_anagram("rat", t = "car") == False