class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # Brute Force - Time = O(n^2), space = O(1) - TLE
        # maxi = 1
        # n = len(s)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         sub_str = s[i: j+1]
        #         if len(sub_str) == len(set(sub_str)):
        #             maxi = max(maxi, len(sub_str))
        # return maxi

        # Sliding window = time = O(n), space = O(1)
        n = len(s)
        # Edge case
        if n == 0 or n == 1:
            return n
        l, r = 0, 1
        present = [s[0]]
        maxi = 1
        while l < r and r < n:
            while l < r and present and s[r] in present:
                present.pop(0)
                l += 1
            present.append(s[r])
            r += 1
            maxi = max(maxi, (r-l))
        return maxi