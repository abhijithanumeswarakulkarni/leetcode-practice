class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        o = len(word)

        def doesExist():
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        res = backtrack(i, j, 0)
                        if res:
                            return True
            return False
        
        def backtrack(i, j, k):
            if k == o:
                return True
            
            if i >= m or j >= n or board[i][j] != word[k] or i < 0 or j < 0:
                return False
            
            board[i][j] = "#"
            res = False
            for direction in directions:
                res = backtrack(i + direction[0], j + direction[1], k + 1)
                if res:
                    break
            board[i][j] = word[k]
            return res
        
        return doesExist()