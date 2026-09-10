class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        frq = Counter(s)
        n = len(s)
        if n % 2 == 0:
            for value in frq.values():
                if value % 2 != 0:
                    return False  
            return True
        
        canOdd = True
        for value in frq.values():
            if value % 2 != 0:
                if canOdd:
                    canOdd = False
                else:
                    return False
        return True