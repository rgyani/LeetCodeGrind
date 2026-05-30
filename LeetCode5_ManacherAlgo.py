"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

No Intuition: Manacher's algo https://www.youtube.com/watch?v=ei7qghJEj4Y

To find all palindromes, you'd normally center at each character and expand outward — that's O(n²).
Manacher's does it in O(n) by reusing work you've already done.


Key Insight: Palindromes Inside Palindromes

If you know a big palindrome exists, any palindromes inside it are mirrored on the other side.
Big palindrome:   [ a b a c a b a ]
                        ↑ center C
Mirror rule: whatever palindrome exists at position i on the right,
             its mirror at (2*C - i) on the left has the same radius!

So instead of expanding from scratch every time, you copy the mirror's answer and only expand further if needed.

Step 1: Handle Even-Length Palindromes
Insert # between every character so all palindromes become odd-length:
"abba"  →  "#a#b#b#a#"   # length changed from 4 to 9
"aba"   →  "#a#b#a#"     # length changed from 3 to 7

Now you only need to handle one case (odd).

Step 2: The P Array
Build an array P where P[i] = radius of the longest palindrome centered at i.
String:  # a # b # b # a #
Index:   0 1 2 3 4 5 6 7 8
P[i]:    0 1 0 1 4 1 0 1 0
                 ↑
            P[4]=4 means palindrome of radius 4 → "abba"

Step 3: The Algorithm (with the mirror trick)
Track two things:

C = center of the rightmost palindrome found so far
R = right boundary of that palindrome

for each position i:
    mirror = 2*C - i          # mirror of i around C

    if i < R:
        P[i] = min(R - i, P[mirror])   # reuse mirror's value!
    else:
        P[i] = 0

    # Try to expand further
    while s[i + P[i] + 1] == s[i - P[i] - 1]:
        P[i]++

    # Update C and R if we expanded past R
    if i + P[i] > R:
        C = i
        R = i + P[i]
The min(R - i, P[mirror]) line is the heart of the algorithm:

If the mirror's palindrome fits inside the big one → copy it exactly
If it touches/exceeds the boundary → we can guarantee up to R - i, then must check further


Why O(n)?
The pointer R only ever moves right, never left. Every character is "expanded over" at most once. So the total work is linear.


Quick Visual Walkthrough
s = "xabacaba"  →  transformed: "#x#a#b#a#c#a#b#a#"

As we scan left to right:
- Find palindrome at 'c' (center): "abacaba", radius = 7
- Now for positions to the right of 'c':
  - 'a' after c mirrors 'a' before c  → P known instantly
  - 'b' after c mirrors 'b' before c  → P known instantly
  - No expansion needed → O(1) per character!


x a b a c a b a
        ↑
        C (center)
radius = 3, so R covers: a b a c a b a
Once we've established c as the center with radius 3, for every position to the right of c that falls within R:
1. a (right of c) → mirrors a (left of c) → P already known -> skip
2. b (right of c) → mirrors b (left of c) → P already known -> skip
3. a (at boundary) → mirrors a (leftmost) → hits the boundary, so we copy up to the boundary but then try expanding (which fails immediately since we're at the edge)

So those 3 characters to the right of c were essentially free.
No left-right expansion needed. We just looked up the mirror and moved on.
The only time we actually do work (expand) is when:
* You're outside any known boundary, or
* The mirror's palindrome bumps right up against the boundary — meaning there might be more beyond it
"""


def manacher(s):
    # Transform: "abc" -> "#a#b#c#"
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    P = [0] * n
    C = R = 0  # center and right boundary

    for i in range(n):
        mirror = 2 * C - i

        if i < R:
            P[i] = min(R - i, P[mirror])

        # Expand around i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 \
              and t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1

        # Update center and boundary
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum
    center = P.index(max(P))
    radius = P[center]
    # Convert back to original string indices
    start = (center - radius) // 2
    return s[start : start + radius]

if __name__ == "__main__":
    assert manacher("xabacaba") == "abacaba"
    assert manacher("babad") == "bab"
    assert manacher("cbbd") == "bb"
    assert manacher("racecar") == "racecar"
    assert manacher("raceacar") == "aca"

    assert manacher("a") == "a"
    assert manacher("ac") == "a"
