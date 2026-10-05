class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2 = [num * k for num in nums2]
        count = 0

        for num1 in nums1:
            for num2 in nums2:
                if num1 >= num2 and num1 % num2 == 0:
                    count += 1
        
        return count