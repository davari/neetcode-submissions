class MinStack:
    import math

    def __init__(self):
        self.stack = ['MinStack']
        self.minElements = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minElements) == 0:
            self.minElements.append(val)
        else:
            tmp_min = min(self.minElements[-1], val)
            self.minElements.append(tmp_min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minElements.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElements[-1]
