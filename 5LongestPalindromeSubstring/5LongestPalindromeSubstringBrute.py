# Complexity O(n^3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstr = ""

        # for every possible substring, see if it's a palindrome
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1] and len(substr) > len(maxstr):
                    maxstr = substr
        
        return maxstr