"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on.
A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


Intuition: a is predecessor of ba, but ba is not  predecessor or a
so if we sort and run thru the list
a ->   nothing in map, we store a -> 1
b ->   a in map but is not a precedessor, we store b -> 1
ba ->  a and b are precedessors, have val 1, so ba -> max(map[a], map[b]) + 1
bca -> ba is precedessor,with val 2, we set bca = 2+1
bda -> ba is precedessor,with val 2, we set bda = 2+1
bdca -> bda is precedessor, with val 3, we set bdca = 3+1
"""

def longest_str_chain(words:list[str]) -> int:
    words.sort(key=len)

    def is_predecessor(word1:str, word2:str):

        if len(word2) - len(word1) != 1:
            return False

        i, j = 0,0
        skipped = False
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i+=1
                j+=1
            elif not skipped:
                skipped = True
                j+=1 # skip one char in word2
            else:
                return False
        return True

    map = {}

    max_len = 0
    for word in words:
        chain_len = 1
        for word2, word2_chain_len in map.items():
            if is_predecessor(word2, word):
                chain_len = max(chain_len, word2_chain_len + 1)
        map[word] = chain_len
        max_len = max(max_len, chain_len)

    return max_len

if __name__ == "__main__":
    assert longest_str_chain(words = ["a","b","ba","bca","bda","bdca"]) == 4
    assert longest_str_chain(["xbc","pcxbcf","xb","cxbc","pcxbc"]) ==5
    assert longest_str_chain(["abcd","dbqca"]) == 1
    assert longest_str_chain([""]) == 1
    assert longest_str_chain(["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"]) == 8
