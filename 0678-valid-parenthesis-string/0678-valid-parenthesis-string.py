class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        def solve(index, open_count, dp):
            if open_count < 0:
                return False
                
            if index == n:
                return open_count == 0
            
            if dp[index][open_count] == -1:
                if s[index] == '(':
                    dp[index][open_count] = solve(index + 1, open_count + 1, dp)
                elif s[index] == ')':
                    dp[index][open_count] = solve(index + 1, open_count - 1, dp)
                else:
                    empty = solve(index + 1, open_count, dp)
                    open_par = solve(index + 1, open_count + 1, dp)
                    close_par = solve(index + 1, open_count - 1, dp)
                    dp[index][open_count] = empty or open_par or close_par
            
            return dp[index][open_count]
        
        dp = [[-1] * (n+1) for _ in range(n)]
        return solve(0, 0, dp)