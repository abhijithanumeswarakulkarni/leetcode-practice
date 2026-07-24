class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Freq map - Time = O(n), space = O(n)
        from collections import Counter
        
        # Edge case - If lengths don't match
        if len(s) != len(t):
            return False

        s_freq = Counter(s)
        t_freq = Counter(t)
        for char in s:
            if s_freq[char] == t_freq[char]:
                del s_freq[char]
                del t_freq[char]
            else:
                return False
        return True if (len(s_freq) == 0 and len(t_freq) == 0) else False
