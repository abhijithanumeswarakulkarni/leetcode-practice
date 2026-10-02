class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        hash_set = set(words)
        res = 0
        used = [False] * len(hash_set)

        for index, word in enumerate(words):
            reverse = word[::-1]
            if reverse in words:
                idx = words.index(reverse)
                if index != idx and not used[index] and not used[idx]:
                    used[index] = True
                    used[idx] = True
                    res += 1
        
        return res