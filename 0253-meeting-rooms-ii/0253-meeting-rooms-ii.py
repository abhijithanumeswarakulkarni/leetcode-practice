class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Hmap
        sortedIntervals = list(sorted(intervals, key = lambda x: x[0]))
        hmap = {}
        count = 0
        for interval in sortedIntervals:
            isAvail = False
            for key in hmap:
                if interval[0] >= hmap[key]:
                    isAvail = True
                    hmap[key] = interval[1]
                    break
            if not isAvail:
                count += 1
                hmap[count] = interval[1]
        
        return count