class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # # HMap - Optimised
        # words = {}
        # for idx, word in enumerate(wordsDict):
        #     if word == word1 or word == word2:
        #         if word in words:
        #             words[word].append(idx)
        #         else:
        #             words[word] = [idx]
        
        # mini = float('inf')
        # for x in words[word1]:
        #     for y in words[word2]:
        #         distance = abs(x-y)
        #         if (distance > 0):
        #             mini = min(mini, distance)
        # return mini

        # Like 2 pointers
        first, second = None, None
        mini = float('inf')
        for index, word in enumerate(wordsDict):
            if word == word1:
                if second != None and index != second:
                    mini = min(mini, abs(index - second))
                first = index
            if word == word2:
                if first != None and index != first:
                    mini = min(mini, abs(index - first))
                second = index
        
        return mini

