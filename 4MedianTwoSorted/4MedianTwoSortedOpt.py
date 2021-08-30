# Complexity O(n/2)

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        prev_val = None
        curr_val = None

        comp1 = None
        comp2 = None
        totallen = len(nums1) + len(nums2)
        for i in range(totallen // 2 + 1):
            prev_val = curr_val

            # comp update
            if comp1 == None and nums1:
                comp1 = nums1.pop(0)
            if comp2 == None and nums2:
                comp2 = nums2.pop(0)

            # merge add, favoring comp1
            if comp2 == None or (comp1 != None and comp1 <= comp2):
                curr_val = comp1
                comp1 = None
            else:
                curr_val = comp2
                comp2 = None

        if totallen % 2 == 0:
            return (prev_val + curr_val)/2
        else:
            return curr_val

sol = Solution()
print(sol.findMedianSortedArrays(
    [0,0,0,0,0],
    [-1,0,0,0,0,0,1]
))