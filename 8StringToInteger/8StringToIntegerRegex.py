# A regex equivalent to atoi
# Complexity unknown because I don't know regex time complexity :P

import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # clean the string
        search = re.compile(r'^\s*[+|-]{0,1}\d+').search(s)
        
        # invalid input
        if search == None:
            return 0

        # clamp value and return
        return max(min(int(search.group(0)), 2**31-1), -2**31)

import sys
sol = Solution()
print(sol.myAtoi(sys.argv[1]))