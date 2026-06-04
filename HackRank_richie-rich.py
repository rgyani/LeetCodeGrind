"""
https://www.hackerrank.com/challenges/richie-rich/problem
Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make.
Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example  is valid,  is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.

Example 1

s=1231
k=2
make 3 replacements to get 9339

s=12321
s=1
make 1 replacement to get 12921

s=3943
s=1
make 1 replacement to get 3993


Intution:
The challenge here is to get palindrome, but u need to get the highest value
so for 1231 if the available cost is 1, u shud return 1331
       1231 if the available cost is 2, u shud return 1991
       1231 if the available cost is 4, u shud return 9999

We use 2 pointers to first count how many replacements are needed
eg in the above case it will be F,T,F,F,
now we make the replacements, again using 2 pointers, if flag[i] or flag[j] is True, make replacement both 9 if cost >=2, else higher of s[i], s[j] if cost == 1, if not cost remains return -1
if there is still some cost remaining, and >=2, start changing from the ends till cost >1

"""
def highestValuePalindrome(s: str, k: int, n: int):
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
