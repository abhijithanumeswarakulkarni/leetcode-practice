class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def solve(index, currStr):
            if index == n:
                if currStr and currStr not in res:
                    res.append(currStr)
                return
            
            for digit in mapping[digits[index]]:
                solve(index+1, currStr + digit)
        
        solve(0, "")
        return res