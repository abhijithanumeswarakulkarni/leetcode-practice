class Solution:
    res = []
    def permute(self, n: int) -> List[List[int]]:
        self.res = []
        def build(curr, prev):
            if len(curr) == n:
                self.res.append(curr)
                return
            
            for val in range(1, n+1):
                if val not in curr:
                    if not prev and val % 2 != 0:
                        build(curr + [val], not prev)
                    if prev and val % 2 == 0:
                        build(curr + [val], not prev)
        
        build([], 0)
        build([], 1)
        self.res.sort()

        return self.res