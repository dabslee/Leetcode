# Complexity O(4^n)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        queue = [""]
        final = []
        while len(queue) > 0:
            curr = queue.pop(0)
            if len(curr) == len(digits):
                final.append(curr)
            else:
                for c in mapping[digits[len(curr)]]:
                    queue.append(curr+c)
        return final

sol = Solution()
print(sol.letterCombinations("23"))