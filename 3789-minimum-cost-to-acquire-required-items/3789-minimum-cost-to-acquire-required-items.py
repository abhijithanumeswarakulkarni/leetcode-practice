class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        opt1 = costBoth * max(need1, need2)
        opt2 = cost1 * need1 + cost2 * need2
        min_need = min(need1, need2)
        opt3 = costBoth * min_need + cost1 * (need1 - min_need) + cost2 * (need2 - min_need)

        return min(opt1, opt2, opt3)