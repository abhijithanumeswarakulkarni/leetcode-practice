class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # Brute Force - Time = O(n^2), space = O(1) - TLE
        # n = len(numbers)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # return [-1.-1] # Never reached

        # Two pointer - Time = O(n), space = O(1)
        i = 0
        j = len(numbers) - 1
        while i < j:
            add = numbers[j] + numbers[i]
            if add == target:
                return [i+1, j+1]
            if add < target:
                i += 1
            else:
                j -= 1
        return [-1, -1] # Again never reached
