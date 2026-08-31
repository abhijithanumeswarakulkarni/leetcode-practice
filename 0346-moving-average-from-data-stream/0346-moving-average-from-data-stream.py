class MovingAverage:
    window = None
    size = None

    def __init__(self, size: int):
        self.window = []
        self.size = size

    def next(self, val: int) -> float:
        self.window.append(val)
        if len(self.window) > self.size:
            self.window.pop(0)
        
        total = sum(self.window)
        k = len(self.window)
        return total / k



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)