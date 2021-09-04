def modNumeral(num):
    if num < 4:
        return "I" * num, 0
    if num < 5:
        return "IV", num % 4
    if num < 9:
        return "V" * (num // 5), num % 5
    if num < 10:
        return "IX", num % 9
    if num < 40:
        return "X" * (num // 10), num % 10
    if num < 50:
        return "XL", num % 40
    if num < 90:
        return "L", num % 50
    if num < 100:
        return "XC", num % 90
    if num < 400:
        return "C" * (num // 100), num % 100
    if num < 500:
        return "CD", num % 400
    if num < 900:
        return "D", num % 500
    if num < 1000:
        return "CM", num % 900
    return "M" * (num // 1000), num % 1000
    
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        while num > 0:
            addend, num = modNumeral(num)
            ans.append(addend)
        return ''.join(ans)

sol = Solution()
print(sol.intToRoman(20))