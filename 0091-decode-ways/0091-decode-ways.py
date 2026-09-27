class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        hmap = {}
        for key in range(1, 27):
            hmap[str(key)] = chr(ord('A') + key - 1)
        
        def solve(index, curr_key, dp):
            if index == n:
                print(curr_key)
                return 1 if (curr_key and curr_key in hmap) else 0
            
            if curr_key and curr_key not in hmap:
                return 0
            
            if (index, curr_key) not in dp:
                opt1 = 0
                updated_key = curr_key + s[index]
                if updated_key in hmap:
                    opt1 = solve(index+1, "", dp)
                opt2 = solve(index+1, updated_key, dp)

                dp[(index, curr_key)] = opt1 + opt2
            
            return dp[(index, curr_key)]

        dp = {}
        res = solve(0, "", dp)
        print(dp)
        return res