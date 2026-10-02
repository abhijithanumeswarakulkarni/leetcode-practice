class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        prev = ""
        n = len(target)
        idx = 0

        while idx < n:
            curr = "a"
            res.append(prev + curr)
            while curr != target[idx]:
                curr = chr(ord('a') + (ord(curr) - ord('a') + 1) % 26)
                res.append(prev + curr)
            prev += curr
            idx += 1
        
        return res