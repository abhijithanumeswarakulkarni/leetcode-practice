class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.idx = -1
        self.remove_idx = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        updated_idx = (self.idx + 1) % self.size
        
        if self.queue[updated_idx] == -1:
            self.queue[updated_idx] = value
            self.idx = updated_idx
            return True

        return False

    def deQueue(self) -> bool:
        updated_rmv_idx = (self.remove_idx + 1) % self.size
        
        if self.queue[updated_rmv_idx] != -1:
            self.queue[updated_rmv_idx] = -1
            self.remove_idx = updated_rmv_idx
            return True
        
        return False


    def Front(self) -> int:
        return self.queue[(self.remove_idx + 1) % self.size]

    def Rear(self) -> int:
        return self.queue[self.idx]

    def isEmpty(self) -> bool:
        return self.idx == self.remove_idx and self.queue[self.idx] == -1

    def isFull(self) -> bool:
        if self.idx == self.remove_idx and self.queue[self.idx] == -1:
            return False
            
        if self.idx > self.remove_idx:
            return self.idx - self.remove_idx == self.size
        
        return (self.size - self.remove_idx - 1) + (self.idx + 1) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()