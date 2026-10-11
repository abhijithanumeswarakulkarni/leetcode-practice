class Solution:
    def countAndSay(self, n: int) -> str:
        def solve(idx):
            if idx == 1:
                return '1'
            
            s = solve(idx-1)
            res = ""
            k = len(s)
            i = 0
            
            while i < k:
                curr = s[i]
                j = i + 1
                while j < k and s[j] == s[i]:
                    j += 1
                res += str(j-i) + curr
                i = j
                
            return res

        return solve(n)