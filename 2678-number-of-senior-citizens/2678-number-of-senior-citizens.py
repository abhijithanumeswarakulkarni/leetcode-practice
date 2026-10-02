class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for detail in details:
            if int(detail[11]) > 6 or (int(detail[11]) == 6 and int(detail[12]) > 0):
                res += 1
        
        return res