class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals = list(sorted(intervals, key=lambda x: x[0]))
        for index, intvl in enumerate(intervals[:-1]):
            if intervals[index+1][0] < intvl[1]:
                return False
        return True