class TwoSum:

    def __init__(self):
        # # Brute force - TLE
        # self.arr = []

        self.hmap = {}
        self.index = 0

    def add(self, number: int) -> None:
        # self.arr.append(number)
        if number not in self.hmap:
            self.hmap[number] = [self.index]
        else:
            self.hmap[number].append(self.index)
        self.index += 1

    def find(self, value: int) -> bool:
        # for i in range(len(self.arr)-1):
        #     for j in range(i+1, len(self.arr)):
        #         if self.arr[i] + self.arr[j] == value:
        #             return True
        # return False
        for x in reversed(sorted(self.hmap.keys())):
            if (value-x) in self.hmap:
                if (value-x) == x :
                    return len(self.hmap[value-x]) >= 2
                return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)