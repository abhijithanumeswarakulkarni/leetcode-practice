class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m, n = len(spells), len(potions)
        potions.sort()

        def binSearch(spell):
            lo, hi = 0, n-1
            idx = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                prod = spell * potions[mid]
                if prod >= success:
                    idx = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return idx
        
        res = []
        for spell in spells:
            j = binSearch(spell)
            if j != -1:
                res.append(n-j)
            else:
                res.append(0)
        
        return res