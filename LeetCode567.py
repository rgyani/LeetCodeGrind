"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Intuition:
We use sliding window here, and just check the frequency of s1 in s2
just a small improvement is, instead of starting from 0 and adding a character at a time, we start with window_count = s2[:l1] and i in range (l1, l2)
each time we keep the window size SAME and remove left and right characters from the window_count
"""

from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    l1, l2 = len(s1), len(s2)
    if l1 > l2:
        return False


    # we take N=len(s1) elements of s2, and their frequency
    # if they have the same frequency as elements of s1, we return True
    # if not, we shift both left and right pointers + 1

    # s1 frequency
    s1_counts = Counter(s1)
    # s2: current window frequency
    window_counts = Counter(s2[:l1])

    if s1_counts == window_counts:
        return True

    # else, slide the window, removing and adding character from s2
    for i in range(l1, l2):
        char_entering = s2[i]
        char_leaving = s2[i-l1]

        window_counts[char_entering] += 1
        window_counts[char_leaving] -= 1
        if window_counts[char_leaving] == 0:
            del window_counts[char_leaving]

        if s1_counts == window_counts:
            return True
    return False


if __name__ == "__main__":
    assert check_inclusion("ab", "eidbaooo") == True
    assert check_inclusion("ab", "eidboaoo") == False
