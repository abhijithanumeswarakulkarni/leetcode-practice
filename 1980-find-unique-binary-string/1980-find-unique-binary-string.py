class Solution:
    res = ""
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)

        def solve(k, curr_str):
            if k == 0:
                if curr_str not in nums:
                    self.res = curr_str
                return
            
            opt1 = solve(k-1, curr_str + '0')
            opt2 = solve(k-1, curr_str + '1')
        
        solve(n, "")
        return self.res