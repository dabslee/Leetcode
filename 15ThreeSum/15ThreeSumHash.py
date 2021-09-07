# Complexity O(n^2)

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
        nums = new_nums

        # create the dct {num : index}
        dct = {}
        for i, num in enumerate(nums):
            if num in dct:
                dct[num].append(i)
            else:
                dct[num] = [i]

        # for each pair, check if needed third val is in dct
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                val = -nums[i]-nums[j]
                if val in dct:
                    for k in dct[val]:
                        if k > j:
                            triplets.add(tuple(
                                sorted(
                                    [nums[i], nums[j], nums[k]])
                                )
                            )
        
        return list(triplets)