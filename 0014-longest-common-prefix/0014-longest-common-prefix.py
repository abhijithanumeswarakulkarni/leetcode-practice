class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxPossible = min(strs, key=len)
        k = len(maxPossible)
        n = len(strs)
        for i in range(k, 0, -1):
            prefix = maxPossible[:i]
            notFound = False
            for st in strs:
                if prefix != st[:i]:
                    notFound = True
                    break
            if not notFound:
                return prefix
        return ""