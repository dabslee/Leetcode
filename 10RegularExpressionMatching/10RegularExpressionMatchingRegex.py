import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rgx = re.compile(p)
        return rgx.fullmatch(s) != None

sol = Solution()
print(sol.isMatch("mississippi", "mis*is*p*."))