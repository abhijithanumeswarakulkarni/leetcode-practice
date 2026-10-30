class FrequencyTracker:

    def __init__(self):
        self.hmap = {}
        self.frq_map = {}

    def update_frq_map(self, frq):
        if not self.frq_map[frq]:
            del self.frq_map[frq]

    def add(self, number: int) -> None:
        curr_frq = 0
        if number in self.hmap:
            curr_frq = self.hmap[number]
            self.frq_map[curr_frq].remove(number)
            self.update_frq_map(curr_frq)
            curr_frq += 1
        else:
            curr_frq = 1
        self.hmap[number] = curr_frq
        if curr_frq in self.frq_map:
            self.frq_map[curr_frq].append(number)
        else:
            self.frq_map[curr_frq] = [number]

    def deleteOne(self, number: int) -> None:
        if number in self.hmap:
            curr_frq = self.hmap[number]
            self.frq_map[curr_frq].remove(number)
            self.update_frq_map(curr_frq)
            curr_frq -= 1
            if curr_frq == 0:
                del self.hmap[number]
            else:
                self.hmap[number] = curr_frq
                if curr_frq in self.frq_map:
                    self.frq_map[curr_frq].append(number)
                else:
                    self.frq_map[curr_frq] = [number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.frq_map


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)