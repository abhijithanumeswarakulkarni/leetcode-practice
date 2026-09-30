class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n = len(intervals)
        i = 0
        while i < n:
            if intervals[i][0] >= newInterval[0]:
                break
            i += 1
        intervals = intervals[:i] + [newInterval] + intervals[i:]
        
        stack = []
        for intvl in intervals:
            if not stack or stack[-1][1] < intvl[0]:
                stack.append(intvl)
            else:
                lastIntvl = stack.pop()
                stack.append([min(lastIntvl[0], intvl[0]), max(lastIntvl[1], intvl[1])])
        return stack