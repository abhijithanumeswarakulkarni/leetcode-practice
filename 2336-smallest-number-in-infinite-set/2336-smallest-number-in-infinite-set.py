class SmallestInfiniteSet:
    popped = None
    small = None
    def __init__(self):
        self.popped = []
        self.small = 1

    def popSmallest(self) -> int:
        self.popped.append(self.small)
        while self.small in self.popped:
            self.small += 1
        return self.popped[-1]

    def addBack(self, num: int) -> None:
        if num in self.popped:
            idx = 0
            n = len(self.popped)
            while idx < n:
                if self.popped[idx] == num:
                    break
                idx += 1
            self.popped.pop(idx)
            if num < self.small:
                self.small = num


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)