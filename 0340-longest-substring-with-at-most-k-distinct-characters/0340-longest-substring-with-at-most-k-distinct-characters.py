class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # # Brute Force - Time = O(n^2), space = O(1) - TLE
        # n = len(s)
        # res = 0
        # i = 0
        # while i < n:
        #     chars = set()
        #     j = i
        #     while j < n:
        #         if s[j] not in chars:
        #             chars.add(s[j])
        #         if len(chars) > k:
        #             break
        #         j += 1
        #     res = max(res, (j-i))
        #     i += 1
        # return res

        # Sliding window - Time = O(n), space = O(1)
        n = len(s)
        if n == 0 or k == 0:
            return 0
        res = 0
        l, r = 0, 0
        chars = {}
        while r < n:
            curr_char = s[r]
            if curr_char in chars:
                chars[curr_char] += 1
            else:
                while len(chars) >= k:
                    if chars[s[l]] > 1:
                        chars[s[l]] -= 1
                    else:
                        del chars[s[l]]
                    l += 1
                chars[curr_char] = 1
            res = max(res, (r-l+1))
            r += 1

        return res