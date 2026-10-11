class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # DP
        n = len(startTime)
        jobs = [(startTime[index], endTime[index], profit[index]) for index in range(n)]
        jobs.sort(key= lambda item: item[0])

        # def solve(index, dp):
        #     if index == n:
        #         return 0
            
        #     if dp[index] == -1:
        #         not_pick = solve(index + 1, dp)
        #         j = index
        #         while j < n and jobs[j][0] < jobs[index][1]:
        #             j += 1
        #         pick = jobs[index][2] + solve(j, dp)

        #         dp[index] = max(pick, not_pick)
            
        #     return dp[index]
        
        # dp = [-1] * n
        # return solve(0, dp)

        dp = [-1] * (n + 1)
        dp[n] = 0
        starts = [job[0] for job in jobs]

        for index in range(n-1, -1, -1):
            not_pick = dp[index+1]
            j = bisect_left(starts, jobs[index][1])
            pick = jobs[index][2] + dp[j]
            dp[index] = max(pick, not_pick)
        
        return dp[0]