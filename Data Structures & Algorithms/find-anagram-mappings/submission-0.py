class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_dict = {}
        index_mapping = []

        for i, num in enumerate(nums2):
            if num in nums2_dict:
                nums2_dict[num].append(i)
            else:
                nums2_dict[num] = [i]

        for num in nums1:
            index_mapping.append(nums2_dict[num][0])

        return index_mapping