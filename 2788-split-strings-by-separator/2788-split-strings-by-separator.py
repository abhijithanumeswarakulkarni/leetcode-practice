class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # Brute Force - Time = O(n*k), space = O(1) - k = # of maximum splits of a word
        res = []
        for word in words:
            word_split = word.split(separator)
            for split in word_split:
                if split:
                    res.append(split)
        return res