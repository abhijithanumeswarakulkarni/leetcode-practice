class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for intvl in intervals[1:]:
            if prevEnd <= intvl[0]:
                prevEnd = intvl[1]
            else:
                res += 1
                prevEnd = min(prevEnd, intvl[1])
            
        return res    