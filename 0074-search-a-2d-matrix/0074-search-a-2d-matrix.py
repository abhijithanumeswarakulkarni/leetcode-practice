class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # Brute Force - Time = O(m*n), space = O(1)
        # m, n = len(matrix), len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True
        # return False

        # Binary Search
        def bin_search(arr):
            lo, hi = 0, len(arr)
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1
        
        m = len(matrix)
        target_row = -1
        for i in range(m):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                target_row = i
                break
        
        if target_row == -1:
            return False
        
        target_col = bin_search(matrix[target_row])
        return True if target_col != -1 else False