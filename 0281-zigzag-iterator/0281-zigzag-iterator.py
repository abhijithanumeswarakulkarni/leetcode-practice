class ZigzagIterator:
    combinedVector = None
    idx = None
    totalLength = None

    def __init__(self, v1: List[int], v2: List[int]):
        self.combinedVector = []
        self.idx = 0
        m, n = len(v1), len(v2)
        self.totalLength = m+n
        if m < n:
            i, j = 0, 0
            turn = True
            while i < m:
                if turn:
                    self.combinedVector.append(v1[i])
                    i += 1
                else:
                    self.combinedVector.append(v2[j])
                    j += 1
                turn = not turn
            self.combinedVector += v2[j:]
        else:
            i, j = 0, 0
            turn = True
            while j < n:
                if turn:
                    self.combinedVector.append(v1[i])
                    i += 1
                else:
                    self.combinedVector.append(v2[j])
                    j += 1
                turn = not turn
            self.combinedVector += v1[i:]
        

    def next(self) -> int:
        index = self.idx
        self.idx += 1
        return self.combinedVector[index]

    def hasNext(self) -> bool:
        return self.idx < self.totalLength

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())