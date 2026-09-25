class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        temp = [None] * n
        res = []

        def solve(index, curr_perm):
            if index == n:
                if curr_perm not in res:
                    res.append(curr_perm[:])
                return
            
            for i in range(n):
                if curr_perm[i] != None:
                    continue
                
                curr_perm[i] = nums[index]
                solve(index+1, curr_perm)
                curr_perm[i] = None
        
        solve(0, temp)    
        return res