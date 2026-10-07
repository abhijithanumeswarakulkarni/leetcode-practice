class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for num in range(num1, num2 + 1):
            num = str(num)
            k = len(num)
            if k < 3:
                continue
            waviness = 0
            for i in range(1, k-1):
                if (num[i] > num[i-1] and num[i] > num[i+1]) or (num[i] < num[i-1] and num[i] < num[i+1]):
                    waviness += 1
            res += waviness
        return res