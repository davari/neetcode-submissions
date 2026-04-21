class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_modified = [-1] * len(arr)
        curr_max = float('-inf')
        for i in range(len(arr)-2, -1, -1):
            curr_max = max(arr[i+1], curr_max)
            arr_modified[i] = curr_max
        
        return arr_modified
            
            