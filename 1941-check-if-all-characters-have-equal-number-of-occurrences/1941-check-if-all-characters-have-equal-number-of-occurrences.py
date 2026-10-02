class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frq = Counter(s)

        frq_value = None
        for key in frq:
            if not frq_value:
                frq_value = frq[key]
            
            if frq[key] != frq_value:
                return False
        
        return True