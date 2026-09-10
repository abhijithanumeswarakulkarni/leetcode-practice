class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraphSplit = map(lambda x: x.lower(), paragraph.split(" "))
        frq = {}
        for word in paragraphSplit:
            if word.isalpha():
                if word in frq:
                    frq[word] += 1
                else:
                    frq[word] = 1
            else:
                key = ""
                for letter in word:
                    if letter.isalpha():
                        key += letter
                    elif key:
                        if key in frq:
                            frq[key] += 1
                        else:
                            frq[key] = 1
                        key = ""
                if key:
                    if key in frq:
                        frq[key] += 1
                    else:
                        frq[key] = 1
        
        sortedFrq = list(sorted(frq.items(), key=lambda x: -x[1]))
        for item in sortedFrq:
            if item[0] not in banned:
                return item[0]
        
        return "" # Every word in paragraph is banned