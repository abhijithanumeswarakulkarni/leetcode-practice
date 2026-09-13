class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        joinedS = "".join(s)
        updatedS = " ".join(reversed(joinedS.split(" ")))

        for idx, x in enumerate(updatedS):
            s[idx] = x