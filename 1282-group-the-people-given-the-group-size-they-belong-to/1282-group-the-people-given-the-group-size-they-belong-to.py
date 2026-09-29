class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        hmap = {}
        for index, size in enumerate(groupSizes):
            if size in hmap:
                hmap[size].append(index)
            else:
                hmap[size] = [index]
        
        res = []
        for size in hmap:
            indices = hmap[size]
            n = len(indices)
            index = 0
            while index < n:
                res.append(indices[index: index+size])
                index += size
        
        return res