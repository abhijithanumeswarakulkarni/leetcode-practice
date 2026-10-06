class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hmap = {}
        
        for x in nums1:
            idx, val = x
            if idx in hmap:
                hmap[idx].append(val)
            else:
                hmap[idx] = [val]
        
        for x in nums2:
            idx, val = x
            if idx in hmap:
                hmap[idx].append(val)
            else:
                hmap[idx] = [val]
        
        res = []
        for key in hmap:
            res.append([key, sum(hmap[key])])
        res.sort(key=lambda x: x[0])
        return res