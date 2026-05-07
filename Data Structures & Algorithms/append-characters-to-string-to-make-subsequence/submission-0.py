class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return j == len(t), len(t) - j

    def appendCharacters(self, s: str, t: str) -> int:
        isSub, numAppend = self.isSubsequence(s, t)

        if not isSub:
            return numAppend
        else:
            return 0