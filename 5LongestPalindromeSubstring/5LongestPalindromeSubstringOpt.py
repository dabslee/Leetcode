# Complexity O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = [0,0]
        for pivot in range(len(s)):
            # pivot is s[pivot]: [b]abad    baba[d]
            cand_pal = [pivot, pivot]
            i = 1
            while pivot-i >= 0 and pivot+i < len(s) and s[pivot-i] == s[pivot+i]:
                cand_pal = [pivot-i, pivot+i]
                i += 1
            max_pal = cand_pal if cand_pal[1] - cand_pal[0] > max_pal[1] - max_pal[0] else max_pal

            # pivot is between s[pivot] and s[pivot-1]: b.abad    babad.
            cand_pal = [pivot, pivot]
            i = 0
            while pivot-i >= 0 and pivot+i+1 < len(s) and s[pivot-i] == s[pivot+i+1]:
                cand_pal = [pivot-i, pivot+i+1]
                i += 1
            max_pal = cand_pal if cand_pal[1] - cand_pal[0] > max_pal[1] - max_pal[0] else max_pal

        return s[max_pal[0]:(max_pal[1]+1)]

sol = Solution()
print(sol.longestPalindrome("babad"))