class Solution:
    def minimumChairs(self, s: str) -> int:
        # Time = O(n), space = O(1)
        free_chairs = 0
        chairs_req = 0
        for x in s:
            if x == 'E':
                if free_chairs > 0:
                    free_chairs -= 1
                else:
                    chairs_req += 1
            else:
                free_chairs += 1
        return chairs_req