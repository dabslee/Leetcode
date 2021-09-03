# Complexity O(lg n)

class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(x).lstrip("-")[::-1])
        ans *= -1 if x < 0 else 1
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        return ans