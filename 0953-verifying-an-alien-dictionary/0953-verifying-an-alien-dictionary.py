class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {}
        for idx, char in enumerate(order):
            pos[char] = idx

        n = len(words)
        for i in range(n-1):
            for j in range(i+1, n):
                a, b = len(words[i]), len(words[j])
                k, l = 0, 0
                while k < a and l < b:
                    left, right = pos[words[i][k]], pos[words[j][l]]
                    if left < right:
                        break
                    elif left > right:
                        return False
                    else:
                        k += 1
                        l += 1
                if k < a and l == b:
                    return False
        return True