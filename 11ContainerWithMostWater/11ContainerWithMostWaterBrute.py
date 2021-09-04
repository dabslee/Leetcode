# Complexity O(n^2)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        for i1 in range(len(height)):
            for i2 in range(i1, len(height)):
                maxarea = max(maxarea, (i2 - i1) * min(height[i2], height[i1]))
        return maxarea

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))