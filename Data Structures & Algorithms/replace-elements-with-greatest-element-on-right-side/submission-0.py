class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_modified = [-1] * len(arr)

        for i in range(len(arr)):
            if i != len(arr) - 1:
                arr_modified[i] = max(arr[i+1:])

        return arr_modified
            