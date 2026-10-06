class OrderedStream:

    def __init__(self, n: int):
        self.map = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.map[idKey] = value
        res = []
        while self.ptr in self.map:
            res.append(self.map[self.ptr])
            self.ptr += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)