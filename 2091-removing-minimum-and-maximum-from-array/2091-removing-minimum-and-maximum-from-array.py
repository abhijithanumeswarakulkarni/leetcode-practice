class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # # Recursion + DP - TLE
        # mini = min(nums)
        # maxi = max(nums)
        # def check(arr):
        #     return (mini not in arr) and (maxi not in arr)
        
        # def solve(i, j, dp):
        #     if i > j:
        #         return float('inf')
            
        #     if check(nums[i:j]):
        #         return 0
        #     if dp[i][j] == -1:
        #         dp[i][j] = min(1 + solve(i+1, j, dp), 1 + solve(i, j-1, dp))
            
        #     return dp[i][j]
        
        # n = len(nums)
        # dp = [[-1] * (n+1) for _ in range(n+1)]
        # return solve(0, n, dp)

        # Greedy
        mini = min(nums)
        maxi = max(nums)
        i, j = nums.index(mini), nums.index(maxi)
        n = len(nums)

        res = 1
        if i < j:
            res = min((j+1), (n-i), ((i+1) + (n-j)))
        elif i > j:
            res = min((i+1), (n-j), ((j+1) + (n-i)))
        
        return res