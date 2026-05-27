"""
Given a string s, find the length of the longest substring without duplicate characters.

 Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Intuition:
slide thru the list, keeping a map of last position of each character -> note max_length
if u see a repeating character, move left to the last position of that char -> note max_length
"""

def length_of_longest_substring(s: str) -> int:
    # store the LAST seen index of each character
    char_map = {}

    left = 0
    max_length = 0

    # iterate thru the list
    for right in range(len(s)):
        current_char = s[right]

        # if the current char is in char_map, it is a duplicate
        if current_char in char_map:
            # we move left to previous occurrence of the character
            left = max(left, char_map[current_char] + 1)

        char_map[current_char] = right

        # at each point store the max length
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3


