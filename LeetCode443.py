"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].
Example 2:

Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it is a single character.
After modifying the input array in-place, the first character of chars should be ["a"].
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
After modifying the input array in-place, the first 4 characters of chars should be ["a","b","1","2"].

Intution, keep two pointers, i and j to 0,1, increment j till a[i] == a[j], count the diff, then i = j+1, j=i+1
but we need to modify the list also in place

so we keep removing elements fomr the list

"""

def compress(chars:list[str])->int:
    j = 0
    i = 0

    n = len(chars)
    while i < n:
        letter = chars[i]
        count = 1
        while i + count < n and chars[i+count] == letter:
            count += 1

        chars[j] = letter
        j += 1
        if count > 1:
            str_val = str(count)
            chars[j: j + len(str_val)] = list(str_val)
            j += len(str_val)
        i+=count
    return j


if __name__ == "__main__":
    lst = list("aabbcc")
    assert  compress(lst) == 6 and lst == list("a2b2c2")
    lst = list("abcc")
    assert compress(lst) == 4 and lst == list("abc2")
    assert compress(list("abc")) == 3
    lst = list("aaaaaaaaaabc")
    assert compress(lst) == 5 and lst[:3] == list("a10")

