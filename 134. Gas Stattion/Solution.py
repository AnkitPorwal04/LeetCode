class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        fuel = idx = 0
        for i in range(len(gas)):
            fuel += gas[i]-cost[i]
            if fuel<0:
                fuel,idx = 0, i+1
        return idx
