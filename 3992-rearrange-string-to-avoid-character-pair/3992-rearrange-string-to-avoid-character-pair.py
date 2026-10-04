class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        frq = Counter(s)
        middle = ""

        for key in frq:
            if key != x and key != y:
                middle += key * frq[key]
        
        return y * frq[y] + middle + x * frq[x]