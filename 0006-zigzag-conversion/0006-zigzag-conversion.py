class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        n = len(s)

        # Edge case
        if num_rows == 1 or n <= num_rows:
            return s

        direction = 0.  # 0 -> down, 1 -> up
        hmap = {}
        curr_row = 0

        for row in range(num_rows):
            hmap[row] = ""
        
        for idx in range(n):
            hmap[curr_row] += s[idx]
            if not direction:
                curr_row += 1
            else:
                curr_row -= 1
            
            if curr_row == num_rows - 1 or curr_row == 0:
                direction = not direction
        
        return "".join(hmap.values())