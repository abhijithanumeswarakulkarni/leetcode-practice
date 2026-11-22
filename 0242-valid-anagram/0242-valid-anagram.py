class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frq_s = Counter(s)
        frq_t = Counter(t)
        # return frq_s == frq_t

        for key, value in frq_s.items():
            if key not in frq_t or value != frq_t[key]:
                return False
            
            del frq_t[key]
            
        return True if not frq_t else False