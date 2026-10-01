class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []

        for x in address:
            if x == '.':
                res.append('[.]')
            else:
                res.append(x)
        
        return "".join(res)