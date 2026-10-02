class Solution:
    def minTimeToType(self, word: str) -> int:
        n = len(word)
        index = 0
        curr = "a"
        res = 0

        while index < n:
            if curr != word[index]:
                ord_curr, ord_word = ord(curr), ord(word[index])
                if ord_word > ord_curr:
                    counter_clock = (ord_curr - ord('a')) + (ord('z') - ord_word) + 1
                    clock = ord_word - ord_curr
                    res += min(counter_clock, clock)
                else:
                    counter_clock = ord_curr - ord_word
                    clock = (ord('z') - ord_curr) + (ord_word - ord('a')) + 1
                    res += min(counter_clock, clock)
                curr = word[index]
            res += 1
            index += 1
        
        return res