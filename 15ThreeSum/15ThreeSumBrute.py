# Complexity O(n^3)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return list(triplets)

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))