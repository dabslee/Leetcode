# Complexity probably approximately O(n^2)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = set()

        # reduce duplicates -- you only need at most 3 of each
        new_nums = []
        for val in set(nums):
            count = nums.count(val)
            if count > 3:
                count = 3
            for i in range(count):
                new_nums.append(val)

        # create a dict of pair sums
        dct = {}
        for i in range(len(new_nums)):
            for j in range(i+1, len(new_nums)):
                pairsum = new_nums[i]+new_nums[j]
                if pairsum not in dct:
                    dct[pairsum] = []
                dct[pairsum].append((i,j))

        for k in range(len(new_nums)):
            if -new_nums[k] not in dct:
                continue
            for i, j in dct[-new_nums[k]]:
                if k == i or k == j:
                    continue
                triplets.add(tuple(sorted([new_nums[i], new_nums[j], new_nums[k]])))

        return list(triplets)

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))