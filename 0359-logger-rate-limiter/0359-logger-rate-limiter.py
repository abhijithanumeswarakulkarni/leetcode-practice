class Logger:

    def __init__(self):
        self.hmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hmap:
            prev_time_stamp = self.hmap[message]
            diff = timestamp - prev_time_stamp
            if diff >= 10:
                self.hmap[message] = timestamp
                return True
            return False
        self.hmap[message] = timestamp
        return True
                


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)