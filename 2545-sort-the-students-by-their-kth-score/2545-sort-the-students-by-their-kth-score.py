class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(score), len(score[0])
        scores = [(score[i][k], i) for i in range(m)]
        res = []

        sorted_scores = list(sorted(scores, key=lambda x: x[0], reverse=True))
        for _, index in sorted_scores:
            res.append(score[index])
        
        return res