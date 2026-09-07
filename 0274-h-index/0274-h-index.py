class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = list(sorted(citations))
        n = len(citations)
        maxi = citations[-1]

        for currIdx in range(maxi, -1, -1):
            count = 0
            for i in range(n):
                if citations[i] >= currIdx:
                    count += 1
            if count >= currIdx:
                return currIdx
        
        return 1