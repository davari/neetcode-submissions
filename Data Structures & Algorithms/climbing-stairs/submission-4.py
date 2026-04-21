class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2

    #     return self.climbStairs(n-1) + self.climbStairs(n-2)
    def climbStairs(self, n: int, memo: dict = {}) -> int:
        if n == 1:
            memo[1] = 1
            return 1
        elif n == 2:
            memo[2] = 2
            return 2

        if n in memo:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return memo[n]
