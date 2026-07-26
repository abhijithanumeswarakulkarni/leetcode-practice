class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # Brute Force
        n = len(nums)
        divisibility_score = [0] * len(divisors)
        max_score = float('-inf')
        for index, divisor in enumerate(divisors):
            count = 0
            for num in nums:
                if num % divisor == 0:
                    count += 1
            divisibility_score[index] = count
            max_score = max(max_score, count)

        res = float('inf')
        for index, score in enumerate(divisibility_score):
            if score == max_score and divisors[index] < res:
                res = divisors[index]
        return res
