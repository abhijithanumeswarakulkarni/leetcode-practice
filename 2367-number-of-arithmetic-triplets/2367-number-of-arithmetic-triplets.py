class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        maxi = max(nums)
        count = 0

        for num in nums:
            if num + 2 * diff > maxi:
                break
            
            if num + diff in nums and num + 2 * diff in nums:
                count += 1
        
        return count