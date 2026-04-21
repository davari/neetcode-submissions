class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # solution 1: 
        # return len(set(nums)) != len(nums)
        
        # solution 2
        tmp_dict = {}

        for i in range(len(nums)):
            if nums[i] in tmp_dict:
                return True
            else:
                tmp_dict[nums[i]] = 1
        return False