class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key = len)
        first, ramaining = strs[0], strs[1:]

        for idx, char in enumerate(first):
            is_prefix = True
            for word in ramaining:
                if word[idx] != char:
                    is_prefix = False
                    break
            if not is_prefix:
                return first[:idx] if idx > 0 else ""
        
        return first