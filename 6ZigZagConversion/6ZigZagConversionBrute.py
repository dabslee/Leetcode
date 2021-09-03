class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows

        curr_row = 0
        direction = 1
        for s_index in range(len(s)):
            rows[curr_row] += s[s_index]
            if (curr_row >= numRows - 1 and direction == 1) or (curr_row <= 0 and direction == -1):
                direction *= -1
            curr_row += direction
        
        finalstr = [''] * len(s)
        finalstr_index = 0
        for row in rows:
            for c in row:
                finalstr[finalstr_index] = c
                finalstr_index += 1
        return ''.join(finalstr)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))