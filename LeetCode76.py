"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Intuition:
For t note the characters and their frequency
Slide thru s, keep expanding window on right till freq(s) == freq(t)
Then keep shrinking the window from left
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    if len(t) == 0 or len(s) == 0:
        return ""

    need = Counter(t)  # chars we need and their required counts
    missing = len(t)  # total characters still needed in window

    best_left, best_right = 0, float("inf")
    left = 0

    for right, char in enumerate(s):
        # Expand: absorb s[right] into the window
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        # Contract: once all chars are covered, shrink from the left
        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1

            # Update best window if this one is smaller
            if right - left < best_right - best_left:
                best_left, best_right = left, right

            # Move left pointer past its current char to search for next window
            need[s[left]] += 1
            missing += 1
            left += 1

    return "" if best_right == float("inf") else s[best_left: best_right + 1]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("DDOBECODEBANC", "ABC") == "BANC"
    assert min_window("DDOBECODABANC", "AABC") == "ABANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
