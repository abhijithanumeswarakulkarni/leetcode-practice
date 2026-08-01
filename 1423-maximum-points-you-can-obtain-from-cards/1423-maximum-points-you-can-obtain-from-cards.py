class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, 0
        n = len(cardPoints)
        for pts in cardPoints[:k]:
            left += pts
        
        maxi = left
        for index in range(k):
            left -= cardPoints[k-index-1]
            right += cardPoints[n-index-1]
            total_sum = left+right
            maxi = max(maxi, total_sum)
        return maxi 