class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)

        def solve(index, temp, dp):
            if index == n:
                return True if (temp and temp in wordDict) or not temp else False
            
            if (index, temp) not in dp:
                opt1 = False
                if temp in wordDict:
                    opt1 = solve(index + 1, s[index], dp)
                opt2 = solve(index + 1, temp + s[index], dp)

                dp[(index, temp)] = opt1 or opt2
            
            return dp[(index, temp)]
            
        dp = {}
        return solve(0, "", dp)