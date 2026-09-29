class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        res = [pref[0]]
        n = len(pref)

        for index in range(1, n):
            res.append(pref[index-1] ^ pref[index])
        
        return res