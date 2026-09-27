class Solution:
    count = 0
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def countPali(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1

        for i in range(n):
            left, right = i, i
            countPali(left, right)
            left, right = i, i+1
            countPali(left, right)
        
        return self.count