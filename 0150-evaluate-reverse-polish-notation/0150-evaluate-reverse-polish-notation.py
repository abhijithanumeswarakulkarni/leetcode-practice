class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for tkn in tokens:
            if tkn in operators:
                element_2 = stack.pop()
                element_1 = stack.pop()
                res = None
                if tkn == '+':
                    res = element_1 + element_2
                elif tkn == '-':
                    res = element_1 - element_2
                elif tkn == '*':
                    res = element_1 * element_2
                else:
                    res = int(str(element_1 / element_2).split('.')[0])
                stack.append(res)
            else:
                stack.append(int(tkn))
        return stack[-1]