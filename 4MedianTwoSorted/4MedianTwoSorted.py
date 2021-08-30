def median(lst: list[int]) -> float:
    length = len(lst)
    if length % 2 == 0:
        return (lst[length // 2] + lst[length // 2 - 1])/2
    else:
        return lst[length // 2]

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # merge the arrays
        comp1 = None
        comp2 = None

        merged = []

        while True:
            # comp1 update and break case
            if not comp1:
                if not nums1:
                    if comp2 != None:
                        merged.append(comp2)
                    merged += nums2
                    break
                comp1 = nums1.pop(0)

            # comp2 update and break case
            if not comp2:
                if not nums2:
                    if comp1 != None:
                        merged.append(comp1)
                    merged += nums1
                    break
                comp2 = nums2.pop(0)

            # merge add, favoring comp1
            if comp1 <= comp2:
                merged.append(comp1)
                comp1 = None
            else:
                merged.append(comp2)
                comp2 = None
        
        return median(merged)