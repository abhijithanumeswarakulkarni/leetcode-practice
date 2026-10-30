class MyCalendar:

    def __init__(self):
        self.times = []

    def book(self, startTime: int, endTime: int) -> bool:
        can_book = True
        for start, end in self.times:
            if (startTime >= start and startTime < end) or (startTime < start and endTime > start):
                can_book = False
                break
        if can_book:
            self.times.append((startTime, endTime))
        return can_book



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)