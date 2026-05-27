"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Intuition:
Find all character frequencies
if ANY character has frequency %2 == 1, we will add 1 at the end (it can be a center character)
for all characters, length += (frequency // 2) * 2
Since for characters with 1 occurence, (frequency // 2) * 2 = 0
"""
from collections import Counter


def longest_palindrome(s: str) -> int:
    if not s:
        return 0

    # Count the frequencies of all characters.
    char_counts = Counter(s)

    length = 0
    has_odd_frequency = False
    for count in char_counts.values():
        # Add the largest even component of the count
        length += (count // 2) * 2

        # Check if there's a remainder we could use for the center
        if count % 2 == 1:
            has_odd_frequency = True

    if has_odd_frequency:
        length += 1

    return length


if __name__ == "__main__":
    assert longest_palindrome("abccccdd") == 7
    assert longest_palindrome("a") == 1
    assert longest_palindrome("aabbcc") == 6
