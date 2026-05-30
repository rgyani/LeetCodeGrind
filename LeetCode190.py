"""
Reverse bits of a given 32 bits signed integer.



Example 1:

Input: n = 43261596
Output: 964176192
Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:
Input: n = 2147483644
Output: 1073741822
Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110

Intution:
1. shift ur result to the left -> r = r << 1
2. get the last bit using n & 1 and it with r
3. right shift n

but u cant do this till n !=0, since the bits might get stuck
eg. for input n = 4.
In 32-bit binary, that looks like this:00000000000000000000000000000100
If we reverse it completely, the 1 should move all the way to the front, resulting in:00100000000000000000000000000000
If we run a loop while n != 0:
* Iteration 1 (n=4): Rightmost bit is 0. res becomes 0. n shifts right to 2.
* Iteration 2 (n=2): Rightmost bit is 0. res becomes 0. n shifts right to 1.
* Iteration 3 (n=1): Rightmost bit is 1. res becomes 1. n shifts right to 0.

The loop stops here because n == 0.
our final res is just 1. we completely missed shifting that 1 all the way to the left to fill out the 32 bits!

"""


def reverse_bits(n: int) -> int:
    res = 0
    for _ in range(32):
        # Shift the result left to make room for the incoming bit
        res = (res << 1) | (n & 1)
        # Shift the input right to prepare the next bit
        n >>= 1
    return res


if __name__ == "__main__":
    assert reverse_bits(43261596) == 964176192
    assert reverse_bits(2147483644) == 1073741822
