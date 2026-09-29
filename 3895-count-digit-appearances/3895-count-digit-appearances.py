class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        digit = str(digit)
        for num in nums:
            count += str(num).count(digit)
        return count