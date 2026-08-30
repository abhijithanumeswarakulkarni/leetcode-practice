class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add, mul = 0, 1
        for digit in str(n):
            add += int(digit)
            mul *= int(digit)
        
        return n % (add + mul) == 0