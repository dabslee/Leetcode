class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack = []
        for c in s:
            if c in dct.values():
                stack.append(c)
            elif c in dct:
                if len(stack) == 0 or stack.pop() != dct[c]:
                    return False
        return len(stack) == 0