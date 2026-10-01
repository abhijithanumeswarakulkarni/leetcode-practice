class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hmap = {}
        for index, value in enumerate(keyboard):
            hmap[value] = index
        
        last = 0
        res = 0
        for char in word:
            res += abs(last - hmap[char])
            last = hmap[char]
        return res