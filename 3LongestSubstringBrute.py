# Complexity O(n^3)

def countFrom(s: str, startIndex: int):
    repeat = ""
    for i in range(startIndex, len(s)):
        if s[i] in repeat:
            return i - startIndex
        else:
            repeat += s[i]
    return i + 1 - startIndex

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        for i in range(len(s)):
            maxlength = max(countFrom(s, i), maxlength)
        return maxlength