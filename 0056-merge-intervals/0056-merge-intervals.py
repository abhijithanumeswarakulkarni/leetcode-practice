class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key= lambda x: x[0])
        stack = [intervals[0]]

        for intvl in intervals[1:]:
            if intvl[0] <= stack[-1][1]:
                last = stack.pop()
                merged_intvl = [min(last[0], intvl[0]), max(last[1], intvl[1])]
                stack.append(merged_intvl)
            else:
                stack.append(intvl)
        
        return stack