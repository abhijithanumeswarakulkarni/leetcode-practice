class Solution:
    def minimumPushes(self, word: str) -> int:
        multiplier, cost = 1, 0
        hmap = {}
        frq = Counter(word)
        sorted_word = list(sorted(frq.items(), key=lambda x: x[1], reverse=True))
        i = 2

        for char, occur in sorted_word:
            if char not in hmap:
                hmap[char] = multiplier
            cost += hmap[char] * occur
            i += 1
            if i == 10:
                multiplier += 1
                i = 2
        
        return cost