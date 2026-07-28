import heapq

class TimeMap:
    hmap = None
    def __init__(self):
        self.hmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            hmap_values = self.hmap[key]
            heapq.heappush(hmap_values, (-timestamp, value))
            self.hmap[key] = hmap_values
        else:
            self.hmap[key] = [(-timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hmap:
            hmap_values = self.hmap[key][:]
            while hmap_values:
                prev_timestamp, value = heapq.heappop(hmap_values)
                if -prev_timestamp <= timestamp:
                    return value
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)