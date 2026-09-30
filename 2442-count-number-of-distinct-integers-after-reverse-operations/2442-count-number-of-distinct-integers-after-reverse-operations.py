class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        reverse = []
        for num in nums:
            reverse.append(int(str(num)[::-1]))
        return len(set(nums + reverse))