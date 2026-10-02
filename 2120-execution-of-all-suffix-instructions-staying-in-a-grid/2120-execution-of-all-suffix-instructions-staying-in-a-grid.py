class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        m = len(s)
        res = [0] * m
        directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

        for index in range(m):
            i, j = startPos
            total = 0
            k = index
            while k < m:
                direction = directions[s[k]]
                i += direction[0]
                j += direction[1]
                if i >= 0 and i < n and j >= 0 and j < n:
                    total += 1
                else:
                    break
                k += 1
            res[index] = total

        return res