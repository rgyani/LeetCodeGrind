"""
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Intuition:
We could find character with max frequency and try to get other characters aligned, but it wont work
Instead, we create a sliding window, and in each window, we check if chars_to_replace = window_length - most_frequent_char > k
if yes, we shrink the window from left, while decreasing the counters,
else, we note the max_window_size and continue expanding the window to the right 
"""


def character_replacement(s: str, k: int) -> int:
    if not s:
        return 0

    # within the window, we count the frequency of each character
    count = {}
    result = 0
    max_freq = 0
    left = 0

    for right,ch in enumerate(s):
        # we note the count of each character
        count[ch] = count.get(ch, 0) + 1

        # also the character which occurs most frequently in this window
        max_freq = max(max_freq, count[ch])

        # if in this window, we have received the required result
        if right - left + 1 - max_freq > k:
            # we shrink the window from left
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AABBBCCCCCC", 2) == 8
    assert character_replacement("AAAA", 0) == 4
