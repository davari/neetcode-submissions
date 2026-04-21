class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        element_counter = {}
        for num in nums:
            if num in element_counter:
                return True
            else:
                element_counter[num] = 1
        return False