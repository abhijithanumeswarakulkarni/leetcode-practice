class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hmap = {}
        for item in knowledge:
            key, value = item[0], item[1]
            hmap[key] = value
        
        print(hmap)
        res = ""
        isKey = False
        key = ""
        for x in s:
            if x == '(':
                isKey = True
            elif x == ')':
                isKey = False
                if key in hmap:
                    res += hmap[key]
                else:
                    res += '?'
                key = ""
            else:
                if isKey:
                    key += x
                else:
                    res += x
        return res
            
