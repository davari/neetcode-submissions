class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # solution 1: O(n^2)
        # for j in range(len(nums)):
        #     for i in range(j):
        #         if i != j and nums[i]+nums[j]==target:
        #             return [i, j]
        
        # # solution 2: O(n)
        # tmp_dict = {}
        # for i in range(len(nums)):
        #     tmp_dict[nums[i]] = i

        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in tmp_dict and tmp_dict[nums[i]] != tmp_dict[diff]:
        #         ind1 = i
        #         ind2 = tmp_dict[diff]
        #         return [min(ind1, ind2), max(ind1, ind2)]

        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]