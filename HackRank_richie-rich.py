"""
https://www.hackerrank.com/challenges/richie-rich/problem
Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example  is valid,  is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.

Example


Make  replacements to get .



Make  replacement to get .

Function Description

Complete the highestValuePalindrome function in the editor below.

highestValuePalindrome has the following parameter(s):

string s: a string representation of an integer
int n: the length of the integer string
int k: the maximum number of changes allowed
Returns

string: a string representation of the highest value achievable or -1
Input Format

The first line contains two space-separated integers,  and , the number of digits in the number and the maximum number of changes allowed.
The second line contains an -digit string of numbers.

Constraints

Each character  in the number is an integer where .
"""
def do_tenent(s: str, k: int, n: int):
    chars = list(s)

    # Track which indices were modified in the first pass
    altered = [False] * n

    # Force the string to be a palindrome with minimum changes
    left = 0
    right = n - 1
    while left < right:
        if chars[left] != chars[right]:
            # Take the maximum of the two to minimize initial cost
            max_ch = max(chars[left], chars[right])
            chars[left] = chars[right] = max_ch
            altered[left] = altered[right] = True
            k -= 1
        left += 1
        right -= 1

    # If we exceeded allowed changes just to make it a palindrome
    if k < 0:
        return "-1"

    # Maximize the palindrome value using remaining 'k'
    left = 0
    right = n - 1
    while left < right:
        if k <= 0:
            break

        if chars[left] != '9':
            # Case A: It was already altered once. Changing it to '9' costs 1 more.
            # Case B: It wasn't altered, but we have enough budget (k >= 2) to change both sides.
            if altered[left] and k >= 1:
                chars[left] = chars[right] = '9'
                k -= 1
            elif not altered[left] and k >= 2:
                chars[left] = chars[right] = '9'
                k -= 2

        left += 1
        right -= 1

    # Case 3: Odd length string and we have 1 change left for the center element
    if n % 2 != 0 and k >= 1:
        chars[n // 2] = '9'

    return "".join(chars)

""""
3143

3443, 1
9443, 3


"""
# Test cases
cases = [
    {'s': '1231', 'k': 3, 'n': 4, 'result': '9339'},
    {'s': '12321', 'k': 1, 'n': 5, 'result': '12921'},
    {'s': '932239', 'k': 2, 'n': 6, 'result': '992299'},
    {"s": "128392759430124", "n": 15, "k": 8, "result": "929394959493929"},
    {'s': '0', 'k': 1, 'n': 1, 'result': '9'},
    {'s': '82272', 'k': 2, 'n': 5, 'result': '87278'},
    {'s': '082272', 'k': 3, 'n': 6, 'result': '982289'},
    {'s': '3943', 'k': 1, 'n': 4, 'result': '3993'},
    {'s': '092282', 'k': 3, 'n': 6, 'result': '992299'},
    {'s': '0011', 'k': 1, 'n': 4, 'result': '-1'},
    {'s': '0', 'k': 0, 'n': 1, 'result': '0'},
    {'s': '3943', 'k': 1, 'n': 4, 'result': '3993'},
    {'s': '092282', 'k': 3, 'n': 6, 'result': '992299'},
    {'s': '0011', 'k': 1, 'n': 4, 'result': '-1'},
    {'s': '3943', 'k': 4, 'n': 4, 'result': '9999'},
]

# Test Execution
for i, case in enumerate(cases):
    res = do_tenent(case["s"], case["k"], case["n"])
    print("Your result for case {}: {}: {}  , correct result: {}".format(i, case["s"], res, case["result"]))
    assert case["result"] == res
