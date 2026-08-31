class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Freq map
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        
        n = len(nums)
        res = []
        for key, value in freq.items():
            if value > n // 3:
                res.append(key)
        
        return res