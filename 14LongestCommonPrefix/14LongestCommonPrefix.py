# Complexity O(S) where S is the sum of all characters in all strings

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        for i in range(len(strs[0])):
            standard = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != standard:
                    return s[:i]
            i += 1
        return strs[0]

sol = Solution()
sol.longestCommonPrefix(["ab", "a"])