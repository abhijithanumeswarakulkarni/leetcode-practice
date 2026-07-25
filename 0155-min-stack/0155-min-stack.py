class MinStack:
    def __init__(self):
        self.stack = []
        self.mini_value = float('inf')
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.mini_value = min(self.mini_value, value)

    def pop(self) -> None:
        self.stack.pop()
        self.mini_value = min(self.stack) if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()