class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        listS = list(s)
        n = len(s)
        i, j = 0, n-1

        while i < j:
            while i < j and s[i].lower() not in vowels:
                i += 1
            while i < j and s[j].lower() not in vowels:
                j -= 1
            listS[i], listS[j] = listS[j], listS[i]
            i += 1
            j -= 1

        return "".join(listS)