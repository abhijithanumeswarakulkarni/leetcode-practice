class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        frq1, frq2 = Counter(s1.split(" ")), Counter(s2.split(" "))
        m, n = len(frq1), len(frq2)
        
        res = []
        for key in frq1:
            if frq1[key] == 1 and key not in frq2:
                res.append(key)
        
        for key in frq2:
            if frq2[key] == 1 and key not in frq1:
                res.append(key)
        
        return res