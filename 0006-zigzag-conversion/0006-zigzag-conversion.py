class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        # Edge case

        if num_rows == 1:
            return s
            
        n = len(s)
        direction = 0.  # 0 -> down, 1 -> up
        hmap = {}
        curr_row = 0

        for row in range(num_rows):
            hmap[row] = []
        
        for idx in range(n):
            hmap[curr_row].append(s[idx])
            if not direction:
                curr_row += 1
            else:
                curr_row -= 1
            
            if curr_row == num_rows:
                direction = not direction
                curr_row -= 2
            
            if curr_row < 0:
                direction = not direction
                curr_row += 2
        
        res = ""
        for row in hmap.values():
            res += "".join(row)
        return res