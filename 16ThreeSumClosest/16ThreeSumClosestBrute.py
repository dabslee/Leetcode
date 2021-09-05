class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        mindistsum = float('inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    distsum = nums[i]+nums[j]+nums[k]
                    if abs(target - distsum) < abs(target - mindistsum):
                        mindistsum = distsum
        return mindistsum