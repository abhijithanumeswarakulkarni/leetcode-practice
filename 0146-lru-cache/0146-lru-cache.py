class LRUCache:
    freq = None
    data = None
    cap = 0

    def __init__(self, capacity: int):
        self.data = {}
        self.order = deque()
        self.cap = capacity
        self.len = 0

    def get(self, key: int) -> int:
        if key in self.data:
            self.order.remove(key)
            self.order.append(key)
            return self.data[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.data and self.len == self.cap:
            evicted_key = self.order.popleft()
            del self.data[evicted_key]
            self.len -= 1
        
        if key in self.data:
            self.order.remove(key)
        else:
            self.len += 1
        
        self.data[key] = value
        self.order.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)