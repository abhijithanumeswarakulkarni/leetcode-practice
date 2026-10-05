class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = curr_bal = 0

        for index, char in enumerate(s):
            if char == '(':
                curr_bal += 1
            else:
                curr_bal -= 1
                if s[index-1] == '(':
                    score += 2 ** curr_bal
        
        return score