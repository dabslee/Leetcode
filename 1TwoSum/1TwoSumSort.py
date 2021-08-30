# returns the key of a value in a value-sorted pseudo-dict
def binarySearchDict(thedict, thevalue):
    min = 0
    max = len(thedict)

    while min < max:
        print(f"searching from {min} to {max} for {thevalue}")
        mid = (max+min)//2
        if thedict[mid][1] > thevalue:
            max = mid
        else:
            min = mid + 1
            
    if thedict[max - 1][1] == thevalue:
        return thedict[max - 1][0]
    else:
        return None

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # create a complement pseudo-dict (list of (index, complement) tuples)
        comp = []
        for i in range(len(nums)):
            comp.append((i, target - nums[i]))

        # sort the complement dict by value
        comp = sorted(comp, key=lambda x: x[1])
        print(comp)

        # check if each num is in comp
        for i in range(len(nums)):
            compcopy = comp.copy()
            index = binarySearchDict(comp, nums[i])
            print(f"{index}")
            if index != None and index != i:
                return [i, index]

sol = Solution()
print(sol.twoSum([3,2,4], 6))