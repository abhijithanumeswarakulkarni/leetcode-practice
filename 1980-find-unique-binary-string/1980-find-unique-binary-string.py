class Solution:
    res = ""
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)

        def solve(k, curr_str):
            if k == 0:
                if curr_str not in nums:
                    self.res = curr_str
                    return True
                return False
            
            opt1 = solve(k-1, curr_str + '0')
            if opt1:
                return True
            opt2 = solve(k-1, curr_str + '1')
            return opt2
        
        solve(n, "")
        return self.res