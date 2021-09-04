class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        ans = 0
        i = 0
        while i < len(s):
            curr = roman_dict[s[i]]
            if i+1 < len(s) and roman_dict[s[i+1]] > curr:
                ans += roman_dict[s[i+1]] - curr
                i += 2
            else:
                ans += curr
                i += 1
        
        return ans

sol = Solution()
print(sol.romanToInt("MCMXCIV"))