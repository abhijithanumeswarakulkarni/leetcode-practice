class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        for key, value in freq1.items():
            if (key in freq2 and abs(freq1[key] - freq2[key]) > 3) or (key not in freq2 and freq1[key] > 3):
                return False

        for key, value in freq2.items():
            if (key in freq1 and abs(freq1[key] - freq2[key]) > 3) or (key not in freq1 and freq2[key] > 3):
                return False
        
        return True        