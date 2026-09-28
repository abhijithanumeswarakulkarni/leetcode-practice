class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less, great = [], []
        equal = 0
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                great.append(num)
            else:
                equal += 1
        return less + [pivot] * equal + great