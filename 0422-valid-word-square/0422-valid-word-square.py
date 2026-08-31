class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        # Edge case
        maxLen = len(max(words, key=len))
        if n < maxLen:
            return False

        for i in range(n):
            for j, char in enumerate(words[i]):
                if j >= len(words[i]) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True