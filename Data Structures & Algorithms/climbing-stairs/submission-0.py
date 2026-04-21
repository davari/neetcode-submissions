class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0

        if n == 1:
            count += 1
            return 1
        elif n == 2:
            count += 2
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)