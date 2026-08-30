class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Brute force
        currMultiple = k
        while True:
            if currMultiple not in nums:
                return currMultiple
            currMultiple += k
        
        return -1 # Ideally never reached