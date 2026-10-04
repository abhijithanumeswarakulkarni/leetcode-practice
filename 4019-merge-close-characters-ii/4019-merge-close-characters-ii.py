class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        res, k = "", min(k, 26)
        for c in s:
            if c not in res[-k:]:
                res += c
        return res