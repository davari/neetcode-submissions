class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        elements_count = {}

        for num in nums:
            if num in elements_count:
                elements_count[num] += 1
            else:
                elements_count[num] = 1
        
        largest = float('-inf')
        for num in elements_count:
            repetition = elements_count[num]
            if repetition == 1 and num > largest:
                largest = num

        return max(-1, largest)