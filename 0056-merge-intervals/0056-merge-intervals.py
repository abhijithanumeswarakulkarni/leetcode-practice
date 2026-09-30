class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = list(sorted(intervals, key=lambda x: x[0]))
        stack = [intervals[0]]
        
        for intvl in intervals[1:]:
            if stack and stack[-1][1] >= intvl[0]:
                lastIntvl = stack.pop()
                stack.append([min(lastIntvl[0], intvl[0]), max(lastIntvl[1], intvl[1])])
            else:
                stack.append(intvl)
        
        return stack