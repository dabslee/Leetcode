# 

import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        new_s = ['#'] * length
        col_size = 2*numRows-2
        no_col = math.ceil(length / col_size)
        last_col_last_row = (length - 1) % col_size

        s_index = 0
        # row 0
        for col in range(no_col):
            new_s[s_index] = s[col * col_size]
            s_index += 1

        # row 1 - (numRows - 2)
        for row in range(1, numRows - 1):
            # column 0
            new_s[s_index] = s[row]
            s_index += 1

            # column 1 - (no_col - 2); 2 each
            for i in range(1, no_col - 1):
                new_s[s_index] = s[i * col_size - row]
                s_index += 1
                new_s[s_index]  =s[i * col_size + row]
                s_index += 1
            
            # column (no_col - 1)
            new_s[s_index] = s[(no_col - 1) * col_size - row]
            s_index += 1
            if row <= last_col_last_row:
                new_s[s_index] = s[(no_col - 1) * col_size + row]
                s_index += 1

        # row (numRows - 1)
          # column all but last
        for col in range(no_col - 1):
            new_s[s_index] = s[col_size * col + numRows - 1]
            s_index += 1
          # last column
        if numRows - 1 <= last_col_last_row:
            new_s[s_index] = s[col_size * (no_col - 1) + numRows - 1]
            s_index += 1

        return ''.join(new_s)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))