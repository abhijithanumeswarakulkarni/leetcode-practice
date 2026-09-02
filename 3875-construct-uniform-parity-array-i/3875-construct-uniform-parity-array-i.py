class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Brute force
        # Try to make all even
        n = len(nums1)
        isEvenPossible = True
        for i in range(n):
            if nums1[i] % 2 == 0:
                continue
            
            canConvert = False
            
            for j in range(n):
                if j != i:
                    temp = abs(nums1[i] - nums1[j])
                    if temp % 2 == 0:
                        canConvert = True
                        break
            
            if not canConvert:
                isEvenPossible = False
                break
        
        if isEvenPossible:
            return True
        
        # Try odd
        isOddPossible = True
        for i in range(n):
            if nums1[i] % 2 != 0:
                continue
            
            canConvert = False
            
            for j in range(n):
                if j != i:
                    temp = abs(nums1[i] - nums1[j])
                    if temp % 2 != 0:
                        canConvert = True
                        break
            
            if not canConvert:
                isOddPossible = False
                break
        
        if isOddPossible:
            return True
        
        return False