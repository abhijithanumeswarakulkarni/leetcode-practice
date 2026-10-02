class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a, b = s[:n//2], s[n//2:]
        count_a, count_b = 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for x in a:
            if x in vowels:
                count_a += 1
        
        for x in b:
            if x in vowels:
                count_b += 1
        
        return count_a == count_b