class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {}
        for index, x in enumerate(s):
            last_index[x] = index
        
        res = []
        max_last_index = -1
        start = 0
        
        for index, x in enumerate(s):
            max_last_index = max(max_last_index, last_index[x])
            if index == max_last_index:
                res.append(index - start + 1)
                start = index + 1

        return res
            