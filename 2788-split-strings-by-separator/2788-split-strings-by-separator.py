class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # Brute Force
        res = []
        for word in words:
            word_split = word.split(separator)
            for split in word_split:
                if split:
                    res.append(split)
        return res