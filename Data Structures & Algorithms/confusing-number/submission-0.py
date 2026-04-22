class Solution:
    def confusingNumber(self, n: int) -> bool:
        from collections import deque
        
        digit_rotation_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6' 
        }

        string_num = str(n)
        string_num_rotated = deque()
        for c in string_num:
            if c in digit_rotation_map:
                string_num_rotated.appendleft(digit_rotation_map[c])
            else:
                return False
        string_num_rotated = ''.join(string_num_rotated)

        if int(string_num_rotated) != n:
            return True
        else:
            return False