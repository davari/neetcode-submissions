class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        direction = shift[0][0]
        amount = 0
        for d, a in shift:
            if d == direction:
                amount += a
            else:
                amount -= a
        
        if amount < 0:
            direction = 1 - direction
            amount = -amount 
        amount = amount % len(s)

        print(direction, amount)
        if amount == 0:
            return s
        else:
            if direction:
                return s[-amount:] + s[:-amount+len(s)]
            else:
                return s[amount:] + s[:amount]