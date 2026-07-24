class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hashmap + Sorting - Time = O(n*(k*log(k))), space = O(n) - k = length of max str in strs
        hmap = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in hmap:
                hmap[sorted_s].append(s)
            else:
                hmap[sorted_s] = [s]
        return list(hmap.values())