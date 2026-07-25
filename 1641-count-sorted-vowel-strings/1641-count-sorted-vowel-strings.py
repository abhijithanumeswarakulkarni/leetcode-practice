class Solution:
    def countVowelStrings(self, n: int) -> int:
        # # Recursion
        # vowels = ['a', 'e', 'i', 'o', 'u']
        # def solve(k, prev):
        #     if k == 0:
        #         return 1
        #     total = 0
        #     for vowel in vowels:
        #         if not prev:
        #             total += solve(k-1, vowel)
        #         elif vowel >= prev:
        #             total += solve(k-1, vowel)
        #     return total
        
        # return solve(n, '')

        # # DP
        # vowels_priority = [1, 2, 3, 4, 5]
        # def solve(k, prev_priority, dp):
        #     if k == 0:
        #         return 1
            
        #     if dp[k][prev_priority] == -1:
        #         total_ways = 0
        #         for vowel_prio in vowels_priority:
        #             if vowel_prio >= prev_priority:
        #                 total_ways += solve(k-1, vowel_prio, dp)
        #         dp[k][prev_priority] = total_ways
        #     return dp[k][prev_priority]
        
        # dp = [[-1] * 6 for _ in range(n+1)]
        # return solve(n, 0, dp)

        # DP + Space optimization
        dp = [[-1] * 6 for _ in range(n+1)]
        dp[0] = [1] * 6
        vowels_priority = [1, 2, 3, 4, 5]
        for k in range(1, n+1):
            for prev_priority in range(0, 6):
                total_ways = 0
                for vowel_prio in vowels_priority:
                    if vowel_prio >= prev_priority:
                        total_ways += dp[k-1][vowel_prio]
                dp[k][prev_priority] = total_ways
        return dp[n][0]
