class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.len = 0

    def push(self, x: int) -> None:
        if self.len < self.maxSize:
            self.stack.append(x)
            self.len += 1

    def pop(self) -> int:
        if self.len == 0:
            return -1
        
        self.len -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        limit = min(self.len, k)
        for i in range(limit):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)