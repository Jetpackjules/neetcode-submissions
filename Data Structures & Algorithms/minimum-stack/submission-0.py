class MinStack:

    def __init__(self):
        self.stack = []
        self.mins =  []
        self.size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mins:
            if val < self.stack[self.mins[-1]]:
                self.mins.append(self.size)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(0)
        self.size += 1

    def pop(self) -> None:
        self.size -= 1
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.mins[-1]]
        
