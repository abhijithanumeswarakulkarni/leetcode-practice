class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words = list(sorted(words, key=len))
        n = len(words)
        frqs = []
        for idx in range(n-1):
            word = words[idx]
            frqs.append(Counter(word))
        
        res = []
        maxLenWord = words[-1]
        maxFrq = Counter(maxLenWord)
        for ltr in maxLenWord:
            isPresent = True
            mini = maxFrq[ltr]
            for frq in frqs:
                if ltr not in frq:
                    isPresent = False
                    break
                mini = min(mini, frq[ltr])
            if isPresent and ltr not in res:
                res += [ltr] * mini
        return res