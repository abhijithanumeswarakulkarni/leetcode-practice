class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frq = {}
        n = len(s)
        i, j = 0, 0
        maxi = 0
        
        while j < n:
            ele = s[j]
            if ele in frq:
                frq[ele] += 1
            else:
                frq[ele] = 1
            
            while frq[ele] > 1:
                frq[s[i]] -= 1
                i += 1
            
            maxi = max(maxi, (j - i + 1))
            j += 1
        
        return maxi