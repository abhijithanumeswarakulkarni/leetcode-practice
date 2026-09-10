class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        i = 1
        n = len(currentState)

        while i < n:
            if currentState[i] == '+' and currentState[i-1] == '+':
                res.append(currentState[:i-1] + "--" + currentState[i+1:])
            i += 1
        
        return res