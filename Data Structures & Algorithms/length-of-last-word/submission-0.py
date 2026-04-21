class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        substrings = s.split(' ')
        for i in range(len(substrings)-1, -1, -1):
            if len(substrings[i]):
                return len(substrings[i])
        return 0