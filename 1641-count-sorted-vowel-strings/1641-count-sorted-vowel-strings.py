class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Recursion
        vowels = ['a', 'e', 'i', 'o', 'u']
        def solve(k, prev):
            if k == 0:
                return 1
            total = 0
            for vowel in vowels:
                if not prev:
                    total += solve(k-1, vowel)
                elif vowel >= prev:
                    total += solve(k-1, vowel)
            return total
        
        return solve(n, '')
