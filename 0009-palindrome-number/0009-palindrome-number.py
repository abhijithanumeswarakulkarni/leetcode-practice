class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        i, j = 0, len(str_num) - 1
        while i < j:
            if str_num[i] != str_num[j]:
                return False
            i += 1
            j -= 1
        return True