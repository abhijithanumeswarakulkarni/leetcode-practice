class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start = list(map(lambda x: int(x), startTime.split(":")))
        end = list(map(lambda x: int(x), endTime.split(":")))
        startSeconds = start[0] * 3600 + start[1] * 60 + start[2]
        endSeconds = end[0] * 3600 + end[1] * 60 + end[2]

        return endSeconds - startSeconds