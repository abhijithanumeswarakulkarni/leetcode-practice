class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            add = numbers[i] + numbers[j]
            if add > target:
                j -= 1
            elif add < target:
                i += 1
            else:
                return [i+1, j+1]
        
        return [-1, -1] # Should never reach