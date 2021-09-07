class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # reduce duplicates -- you only need at most 4 of each
        # O(n^2)
        new_nums = []
        for val in set(nums):
            count = nums.count(val)
            if count > 4:
                count = 4
            for i in range(count):
                new_nums.append(val)
        nums = new_nums

        # create a twosum:indexpair hashmap
        # O(n^2)
        dct = {}
        twosums = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                val = nums[i] + nums[j]
                if val in dct:
                    dct[val].append((i,j))
                else:
                    dct[val] = [(i,j)]
                    twosums.add(val)
        
        # for each twosum, find the corresponsing twosum and check if
        # there are any combos with distinct indices
        # O(n^6)
        quadruplets = set()
        for twosum in twosums:
            if target-twosum not in twosums:
                continue
            for index_pair_1 in dct[twosum]:
                for index_pair_2 in dct[target-twosum]:
                    if index_pair_1[0] == index_pair_2[0] or index_pair_1[0] == index_pair_2[1] or index_pair_1[1] == index_pair_2[0] or index_pair_1[1] == index_pair_2[1]:
                        continue
                    quadruplet = tuple(sorted([nums[i] for i in index_pair_1 + index_pair_2]))
                    quadruplets.add(quadruplet)
        
        return list(quadruplets)

sol = Solution()
print(sol.fourSum(nums = [1,0,-1,0,-2,2], target = 0))