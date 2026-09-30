class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        res = []
        index = 0
        k = len(target)
        last = 0
        
        for stream in range(1, n+1):
            if index == k:
                break
            
            if stream == target[index]:
                pops = ['Pop'] * (stream - last - 1)
                res += pops
                last = target[index]
                index += 1

            res.append('Push')
        
        return res