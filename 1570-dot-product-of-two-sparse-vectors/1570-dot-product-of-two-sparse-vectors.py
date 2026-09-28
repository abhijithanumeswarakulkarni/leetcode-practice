class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        # self.n = len(nums) - Would need for edge case

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for index, value in enumerate(self.nums):
            product += value * vec.nums[index]
        return product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)