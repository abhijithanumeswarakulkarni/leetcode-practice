class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0, 0
        n = len(s)
        maxVow = float('-inf')
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        while r < n:
            while (r-l+1) > k:
                if s[l] in vowels:
                    count -= 1
                l += 1
            
            if s[r] in vowels:
                count += 1
            
            if (r-l+1) == k:
                maxVow = max(maxVow, count)
            
            r += 1
        
        return maxVow