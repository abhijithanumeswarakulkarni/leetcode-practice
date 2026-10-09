class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if num % 3 != 0:
                div = num // 3
                opt1 = num - (div * 3)
                opt2 = (div + 1) * 3 - num
                count += min(opt1, opt2)
        
        return count