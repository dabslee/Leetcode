# Complexity O(n^3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check each length of substring, stopping when you find a palindrome
        for length in range(len(s), 0 - 1, -1):
            for j in range(0, len(s) - length + 1):
                substr = s[j:j+length]
                # print(f"checking string: {substr}")
                if substr == substr[::-1]:
                    return substr