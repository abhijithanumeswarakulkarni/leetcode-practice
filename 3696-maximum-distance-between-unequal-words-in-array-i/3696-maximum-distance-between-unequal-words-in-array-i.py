class Solution:
    def maxDistance(self, words: List[str]) -> int:
        maxi = 0
        n = len(words)

        for i in range(n-1):
            for j in range(i+1, n):
                if words[i] != words[j]:
                    maxi = max(maxi, (j - i + 1))
        
        return maxi