class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c_counts = {}
        for c in s:
            if c in c_counts:
                c_counts[c] += 1
            else:
                c_counts[c] = 1
        
        count_odds = count_evens = 0
        for c_count in c_counts:
            if c_counts[c_count] % 2:
                count_odds += 1
            else:
                count_evens += 1
        
        if (not(len(s) % 2) and count_odds != 0) or count_odds > 1:
            return False
        return True
        