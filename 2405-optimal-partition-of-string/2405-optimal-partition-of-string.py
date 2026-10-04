class Solution:
    def partitionString(self, s: str) -> int:
        curr_sub = s[0]
        count = 1

        for char in s[1:]:
            if char not in curr_sub:
                curr_sub += char
            else:
                count += 1
                curr_sub = char
        
        return count