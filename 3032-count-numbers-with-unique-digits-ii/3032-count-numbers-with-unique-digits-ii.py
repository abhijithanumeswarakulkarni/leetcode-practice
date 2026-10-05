class Solution:
    def numberCount(self, a: int, b: int) -> int:
        count = 0

        for x in range(a, b+1):
            str_x = str(x)
            if len(str_x) == len(set(str_x)):
                count += 1
        
        return count