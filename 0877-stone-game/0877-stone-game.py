class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Brute force
        n = len(piles)
        alice_score, bob_score = 0, 0
        i, j = 0, n-1
        turn = True
        while i < j:
            optimal_pick = 0
            if piles[i] > piles[j]:
                optimal_pick = piles[i]
                i += 1
            else:
                optimal_pick = piles[j]
                j -= 1
            if turn:
                alice_score += optimal_pick
            else:
                bob_score += optimal_pick

        return alice_score > bob_score