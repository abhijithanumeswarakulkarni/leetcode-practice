class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sortedIntervals = list(sorted(intervals, key=lambda x: (x[0], x[1])))

        i = 0
        n = len(intervals)
        while i < n-1:
            if sortedIntervals[i][1] > sortedIntervals[i+1][0]:
                return False
            i += 1
        
        return True