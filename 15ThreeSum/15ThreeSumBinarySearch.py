# Complexity O(n^2 lg n)

def binarySearch(dct, val):
    left = 0
    right = len(dct) - 1
    while right >= left:
        mid = (right + left) // 2
        if dct[mid] > val:
            right = mid - 1
        elif dct[mid] < val:
            left = mid + 1
        else:
            return mid
    return -1

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = binarySearch(nums[j+1:], 0 - nums[i] - nums[j])
                if k != -1:
                    k += j+1
                    triplets.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return list(triplets)

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))