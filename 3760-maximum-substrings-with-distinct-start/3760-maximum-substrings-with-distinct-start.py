class Solution:
    def maxDistinct(self, s: str) -> int:
        count = 0
        starts = set()

        for x in s:
            if x not in starts:
                count += 1
            starts.add(x)
        
        return count