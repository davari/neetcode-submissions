class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tmp_dictionary = {}
        for c in s:
            if c in tmp_dictionary:
                tmp_dictionary[c] += 1
            else:
                tmp_dictionary[c] = 1

        for c in t:
            if c in tmp_dictionary:
                tmp_dictionary[c] -= 1
            else:
                return False

        return not any(tmp_dictionary.values())