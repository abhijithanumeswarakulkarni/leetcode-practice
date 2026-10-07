class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        dp = [False] * (primeOne * primeTwo + 1)
        dp[0] = True
        res = 1

        for i in range(1, primeOne * primeTwo):
            dp[i] = dp[i - primeOne] or dp[i - primeTwo]
            if not dp[i]:
                res = i
        
        return res