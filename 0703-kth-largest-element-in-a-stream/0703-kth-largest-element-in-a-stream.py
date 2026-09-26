class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = list(reversed(sorted(nums)))
        self.k = k
        self.res = float('-inf')
        self.len = len(self.nums)
        if self.len >= self.k:
            self.res = self.nums[k-1]

    def add(self, val: int) -> int:
        if not self.nums or val < self.nums[-1]:
            self.nums.append(val)
        elif val > self.nums[0]:
            self.nums = [val] + self.nums
        else:
            for index in range(self.len):
                if self.nums[index] <= val:
                    self.nums = self.nums[:index] + [val] + self.nums[index:]
                    break
        self.len += 1
        self.res = self.nums[self.k-1]
        return self.res
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)