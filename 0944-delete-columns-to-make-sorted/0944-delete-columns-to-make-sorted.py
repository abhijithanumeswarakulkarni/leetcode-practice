class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        cols = [[] for _ in range(n)]

        for s in strs:
            for idx, char in enumerate(s):
                cols[idx].append(char)
        
        count = 0
        for col in cols:
            if "".join(sorted(col)) != "".join(col):
                count += 1
        
        return count