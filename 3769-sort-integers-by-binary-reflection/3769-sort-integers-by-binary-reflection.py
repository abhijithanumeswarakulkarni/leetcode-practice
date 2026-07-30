class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            bin_ref = int(str(bin(num))[2:][::-1], 2)
            res.append((bin_ref, num))
        res = list(sorted(res, key=lambda x: (x[0], x[1])))
        return [x[1] for x in res]