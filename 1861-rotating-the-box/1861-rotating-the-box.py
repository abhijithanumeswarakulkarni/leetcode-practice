class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        for i in range(m):
            j = n-2
            while j >= 0:
                if boxGrid[i][j] == '#':
                    k = j
                    while k < n-1 and boxGrid[i][k+1] == '.':
                        boxGrid[i][k], boxGrid[i][k+1] = boxGrid[i][k+1], boxGrid[i][k]
                        k += 1
                j -= 1
        
        res = {}
        for i in range(m-1, -1, -1):
            for j in range(n):
                if j in res:
                    res[j].append(boxGrid[i][j])
                else:
                    res[j] = [boxGrid[i][j]]

        return list(res.values())