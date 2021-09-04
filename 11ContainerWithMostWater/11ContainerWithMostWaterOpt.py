# Complexity O(n lg n)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        height_dict = {i : h for i,h in enumerate(height)}
        height_dict = sorted(height_dict.items(), key = lambda kv : kv[1], reverse=True)

        # for each height, find the max and min i values that meet that
        # height to find the maxarea for that height
        max_area = 0
        min_i = height_dict[0][0]
        max_i = height_dict[0][0]
        for i, h in height_dict:
            if i < min_i:
                min_i = i
            if i > max_i:
                max_i = i
            if (max_i-min_i)*h > max_area:
                max_area = (max_i-min_i)*h

        return max_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))