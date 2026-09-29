class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prevRowLazers, prevRow = -1, -1        
        total = 0
        m = len(bank)

        for index, row in enumerate(bank):
            devices = row.count('1')
            if devices > 0:
                if prevRow != -1:
                    total += prevRowLazers * devices
                prevRow = index
                prevRowLazers = devices
        
        return total
