class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        count = 1
        hmap = {count: intervals[0][1]}

        for intvl in intervals[1:]:
            room_exists = False
            for key in hmap:
                if intvl[0] >= hmap[key]:
                    hmap[key] = intvl[1]
                    room_exists = True
                    break
            if not room_exists:
                count += 1
                hmap[count] = intvl[1]
        
        return count