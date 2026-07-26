class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # Brute force - Time = O(n), space = O(1)
        # Edge case
        if len(set(arr)) == 1:
            return arr[0]
        
        diff = arr[1] - arr[0]
        n = len(arr)
        res = None
        for i in range(2, n):
            if arr[i] - arr[i-1] != diff:
                res = arr[i] - diff
                break
        return res