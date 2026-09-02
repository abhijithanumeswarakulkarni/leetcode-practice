from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frq1 = Counter(word1)
        frq2 = Counter(word2)

        keys1 = list(sorted(frq1.keys()))
        values1 = list(sorted(frq1.values()))

        keys2 = list(sorted(frq2.keys()))
        values2 = list(sorted(frq2.values()))

        if keys1 == keys2 and values1 == values2:
            return True
        
        return False