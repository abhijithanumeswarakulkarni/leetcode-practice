class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_encountered = deque([])
        max_len = 0
        left, right = 0, 0
        n = len(s)

        while right < n:
            while left < right and s[right] in chars_encountered:
                chars_encountered.popleft()
                left += 1
            
            max_len = max(max_len, (right - left + 1))
            chars_encountered.append(s[right])
            right += 1
        
        return max_len