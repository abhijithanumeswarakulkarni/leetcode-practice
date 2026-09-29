class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        m = len(l)
        res = []

        for index in range(m):
            sub = list(sorted(nums[l[index]:r[index]+1]))
            k = r[index] - l[index] + 1
            diff = sub[1] - sub[0]
            is_seq = True
            for j in range(1, k-1):
                if sub[j+1] - sub[j] != diff:
                    is_seq = False
                    break
            res.append(is_seq)
        
        return res