# Complexity O(4^n/sqrt(n))

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        queue = [""]
        while len(queue) > 0:
            s = queue.pop(0)
            opened = s.count("(")
            closed = s.count(")")

            if closed == opened == n:
                ans.append(s)
                continue

            if opened < n:
                queue.append(s + "(")
            if closed < opened:
                queue.append(s + ")")
        return ans

import sys
sol = Solution()
print(sol.generateParenthesis(int(sys.argv[1])))