class Solution:
    def goodIndices(self, s: str) -> List[int]:
        res = []
        n = len(s)
        for index in range(n):
            str_index = str(index)
            k = len(str_index)
            if s[index-k+1: index+1] == str_index:
                res.append(index)
        return res