class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # solution 1: O(n^2)
        for j in range(len(nums)):
            for i in range(j):
                if i != j and nums[i]+nums[j]==target:
                    return [i, j]
        
        # solution 2: O(n)
        tmp_dict = {}
        for i in range(len(nums)):
            tmp_dict[nums[i]] = (i, target-nums[i])

        for num in len(nums):
            if tmp_dict[num][1] in tmp_dict:
                return [tmp_dict[num][0], tmp_dict[tmp_dict[num][1][0]]]
