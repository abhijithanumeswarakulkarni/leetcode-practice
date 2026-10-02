class Solution:
    def maxSameLengthRuns(self, s: str) -> int:
        hmap = {}
        n = len(s)
        i = 0
        while i < n:
            curr_run = s[i]
            j = i + 1
            while j < n and s[j] == s[i]:
                curr_run += s[j]
                j += 1
            if (j-i) in hmap:
                hmap[(j-i)].append(curr_run)
            else:
                hmap[(j-i)] = [curr_run]
            i = j
        
        return len(max(hmap.values(), key=len))