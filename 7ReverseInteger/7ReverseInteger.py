class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(x)[::-1].rstrip("-"))
        ans *= -1 if str(x)[0] == '-' else 1
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        return ans