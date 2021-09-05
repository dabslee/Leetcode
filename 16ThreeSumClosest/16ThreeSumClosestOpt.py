# dynamic programming solution

import copy

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # dynamic programming
        dct = {0:[True, False, False, False]}
        for num in nums:
            dct_copy = copy.deepcopy(dct)
            for key in dct_copy:
                dct[key+num] = [
                    key+num in dct and dct[key+num][0],
                    dct_copy[key][0] | (key+num in dct and dct[key+num][1]),
                    dct_copy[key][1] | (key+num in dct and dct[key+num][2]),
                    dct_copy[key][2] | (key+num in dct and dct[key+num][3])
                ]
                if sum(dct[key+num]) == 0:
                    dct.pop(key+num)
        closest = float('inf')
        for key, val in dct.items():
            if val[3] and abs(key - target) < abs(closest - target):
                closest = key
        return closest

sol = Solution()
print(sol.threeSumClosest(
    nums = [0,2,1,-3],
    target = 1
))