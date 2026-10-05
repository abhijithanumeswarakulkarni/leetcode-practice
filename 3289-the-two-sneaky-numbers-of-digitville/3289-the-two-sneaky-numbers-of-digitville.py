class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # frq = list(sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True))
        # res = [x[0] for x in frq[:2]]
        # return res
        frq = Counter(nums)
        res = []
        for key in frq:
            if frq[key] > 1:
                res.append(key)
        return res
