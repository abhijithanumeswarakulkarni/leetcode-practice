class Solution:
    res = None
    
    def __init__(self):
        self.res = []
    
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        def solve(index, target, curr_bin):
            if target < 0:
                return

            if index == n:
                self.res.append(curr_bin)
                return
            
            zero = solve(index + 1, target, curr_bin + '0')
            if not curr_bin or curr_bin[-1] != '1':
                one = solve(index + 1, target - index, curr_bin + '1')
        
        solve(0, k, "")
        return self.res