class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_unique_index = 1
        for current_index in range(1, len(nums)):
            if nums[current_index] != nums[current_index - 1]:
                nums[current_unique_index] = nums[current_index]
                current_unique_index += 1

        k = current_unique_index

        return k