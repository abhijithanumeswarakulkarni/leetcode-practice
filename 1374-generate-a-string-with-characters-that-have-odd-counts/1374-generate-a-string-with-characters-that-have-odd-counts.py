class Solution:
    def generateTheString(self, n: int) -> str:
        char1 = char2 = chr(random.randint(97, 122))
        
        while char2 == char1:
            char2 = chr(random.randint(97, 122))

        if n % 2 != 0:
            return char1 * n
        
        return char1 * (n-1) + char2