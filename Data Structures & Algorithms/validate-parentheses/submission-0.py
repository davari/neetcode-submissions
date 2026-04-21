class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets_stack = []
        for c in s:
            if c in [')', ']', '}'] and len(open_brackets_stack)==0:
                return False
            elif c in ['(', '[', '{']:
                open_brackets_stack.append(c)
            elif (c == ')' and open_brackets_stack[-1] != '(') or \
                (c == ']' and open_brackets_stack[-1] != '[') or \
                (c == '}' and open_brackets_stack[-1] != '{'):
                return False
            else:
                open_brackets_stack.pop()
                
        if len(open_brackets_stack) == 0:
            return True
        else: 
            return False