class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hmap = {}
        mapped_char = 'a'
        for char in key:
            if char not in hmap and char.isalpha():
                hmap[char] = mapped_char
                mapped_char = chr(ord(mapped_char) + 1)
            if mapped_char == chr(ord('z') + 1):
                break

        res = ""
        for x in message:
            if x.isalpha():
                res += hmap[x]
            else:
                res += x
        return res
        