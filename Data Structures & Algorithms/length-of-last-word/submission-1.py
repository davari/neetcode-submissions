class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx1 = len(s)-1
        while s[idx1] == ' ':
            idx1 -= 1
            if idx1 < 0:
                return 0
        
        idx2 = idx1 - 1
        while s[idx2] != ' ' and idx2 >= 0:
            idx2 -= 1

        return idx1 - idx2