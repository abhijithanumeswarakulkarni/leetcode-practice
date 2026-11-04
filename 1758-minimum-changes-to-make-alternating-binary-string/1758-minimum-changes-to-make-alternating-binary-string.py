class Solution:
    def minOperations(self, s: str) -> int:
        list_s = list(s)
        n = len(s)
        count1 = 0

        for i in range(1, n):
            if list_s[i - 1] == list_s[i]:
                if list_s[i] == '0':
                    list_s[i] = '1'
                else:
                    list_s[i] = '0'
                count1 += 1
        
        list_s = list(s)
        if list_s[0] == '0':
            list_s[0] = '1'
        else:
            list_s[0] = '0'
        count2 = 1
        
        for i in range(1, n):
            if list_s[i - 1] == list_s[i]:
                if list_s[i] == '0':
                    list_s[i] = '1'
                else:
                    list_s[i] = '0'
                count2 += 1
        
        return min(count1, count2)