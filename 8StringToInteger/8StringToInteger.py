# An implementation of atoi without using any native conversion methods
# (except ord, which would not be a conversion method in C)

class Solution:
    def myAtoi(self, s: str) -> int:
        # Read in and ignore any leading whitespace.
        s = s.lstrip()

        # Check if the next character (if not already at the end of the
        # string) is '-' or '+'. Read this character in if it is either.
        if len(s) == 0:
            return 0
        i = 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Read in next the characters until the next non-digit charcter
        # or the end of the input is reached. The rest of the string is
        # ignored.
        start_i = i
        while i < len(s) and s[i] <= '9' and s[i] >= '0':
            i += 1
        str_ans = s[start_i:i]

        # Convert these digits into an integer. If no digits were read,
        # then the integer is 0. Change the sign as necessary.
        ans = 0
        for c in str_ans:
            ans = ans*10 + ord(c) - ord('0')
        ans *= sign

        # If the integer is out of the 32-bit signed integer range, then
        # clamp the integer so that it remains in the range.
        ans = max(min(ans, 2**31-1), -2**31)

        # Return the integer as the final result.
        return ans

import sys
sol = Solution()
print(sol.myAtoi(sys.argv[1]))