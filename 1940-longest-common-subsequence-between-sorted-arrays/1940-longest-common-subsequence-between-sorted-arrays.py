class Solution:
    def longestCommonSubsequence(self, arrays: list[list[int]]) -> list[int]:
        base = min(arrays, key=len)
        res = []

        for element in base:
            present = True
            for array in arrays:
                if element not in array:
                    present = False
                    break
            if present:
                res.append(element)
        
        return res