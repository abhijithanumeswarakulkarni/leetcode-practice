class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_encountered = set()
        max_len = 0
        left, right = 0, 0
        n = len(s)

        while right < n:
            while left < right and s[right] in chars_encountered:
                chars_encountered.remove(s[left])
                left += 1
            
            max_len = max(max_len, (right - left + 1))
            chars_encountered.add(s[right])
            right += 1
        
        return max_len