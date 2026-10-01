class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        frq = Counter(hand)

        while frq:
            start = min(frq.keys())
            frq[start] -= 1
            if frq[start] == 0:
                del frq[start]
            for _ in range(groupSize-1):
                if start + 1 in frq:
                    start += 1
                    frq[start] -= 1
                    if frq[start] == 0:
                        del frq[start]
                else:
                    return False
        
        return True