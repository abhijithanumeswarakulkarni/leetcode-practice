class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_encountered = {}
        max_len = 0
        left, right = 0, 0
        n = len(s)

        while right < n:
            while left < right and s[right] in chars_encountered:
                del chars_encountered[s[left]]
                left += 1
            
            max_len = max(max_len, (right - left + 1))
            chars_encountered[s[right]] = 1
            right += 1
        
        return max_len