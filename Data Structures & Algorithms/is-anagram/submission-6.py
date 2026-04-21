class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = {}
        counter2 = {}
        for c in s:
            if c in counter1:
                counter1[c] += 1
            else:
                counter1[c] = 1

        for c in t:
            if c in counter2:
                counter2[c] += 1
            else:
                counter2[c] = 1
        
        return counter1 == counter2