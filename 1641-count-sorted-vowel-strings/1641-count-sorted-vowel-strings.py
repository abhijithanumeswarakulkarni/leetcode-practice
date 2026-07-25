class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Recursion
        vowels = ['a', 'e', 'i', 'o', 'u']
        def solve(k, temp):
            if k == 0:
                return 1
            total = 0
            for v in vowels:
                if not temp:
                    total += solve(k-1, v)
                elif v >= temp[-1]:
                    total += solve(k-1, temp+v)
            return total
        
        return solve(n, '')
