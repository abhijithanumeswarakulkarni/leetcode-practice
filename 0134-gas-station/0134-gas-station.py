class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        gas_cost = []
        n = len(gas)
        
        for i in range(n):
            gas_cost.append((gas[i], cost[i], i))
        
        gas_cost.sort(reverse=True)

        for gs, cst, index in gas_cost:
            curr_gas = gs - cst
            i = (index+1) % n
            while curr_gas > 0 and i != index:
                curr_gas = curr_gas - cost[i] + gas[i]
                i = (i + 1) % n
            if curr_gas >= 0 and i == index:
                return i
        
        return -1

