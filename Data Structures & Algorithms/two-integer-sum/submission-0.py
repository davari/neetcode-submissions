class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution 1:
        for j in range(len(nums)):
            for i in range(j):
                if i != j and nums[i]+nums[j]==target:
                    return [i, j]
        
        # if len(nums) == 1:
        #     return False
        
        # i = j = 0

        # while i < j and j < len(nums):
        #     if i == j:
        #         j += 1
        #     else