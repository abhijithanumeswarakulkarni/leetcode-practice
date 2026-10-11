class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        k = len(t)
        
        next_dp = [0] * (k + 1)
        next_dp[-1] = 1
        
        for i in range(n-1, -1, -1):
            curr_dp = [0] * (k + 1)
            curr_dp[-1] = 1
            for j in range(k-1, -1, -1):
                pick = 0
                if s[i] == t[j]:
                    pick = next_dp[j + 1]
                not_pick = next_dp[j]
                curr_dp[j] = pick + not_pick
            next_dp = curr_dp
        
        return next_dp[0]
        


