class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = len(flowerbed)

        if flowerbed[0] == 0 and (k == 1 or (k > 1 and flowerbed[1] != 1)):
            n -= 1
            flowerbed[0] = 1

        i = 1
        while i < k-1 and n > 0:
            if flowerbed[i-1] != 1 and flowerbed[i] == 0 and flowerbed[i+1] != 1:
                n -= 1
                flowerbed[i] = 1
            i += 1
        
        if n > 0 and flowerbed[i-1] != 1 and flowerbed[i] != 1:
            n -= 1
            flowerbed[i] = 1
        
        return True if n <= 0 else False