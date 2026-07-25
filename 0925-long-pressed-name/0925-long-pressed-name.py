class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Brute force - time = O(n), space = O(1)
        i, j = 0, 0
        m = len(name)
        n = len(typed)
        while i < m and j < n:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and typed[j] == name[i-1]:
                while j < n and typed[j] == name[i-1]:
                    j += 1
            else:
                return False
        if i == m and j != n:
            while j < n and name[i-1] == typed[j]:
                j += 1
        return True if i == m and j == n else False