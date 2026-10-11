class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")
        res = []

        for word in words[::-1]:
            if word:
                res.append(word)
        
        return " ".join(res)