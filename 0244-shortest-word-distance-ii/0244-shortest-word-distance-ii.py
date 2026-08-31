class WordDistance:
    words = None
    def __init__(self, wordsDict: List[str]):
        self.words = {}
        for index, word in enumerate(wordsDict):
            if word in self.words:
                self.words[word].append(index)
            else:
                self.words[word] = [index]

    def shortest(self, word1: str, word2: str) -> int:
        mini = float('inf')
        word1Idxs = self.words[word1]
        word2Idxs = self.words[word2]
        for x in word1Idxs:
            for y in word2Idxs:
                mini = min(mini, abs(x-y))
        return mini
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)