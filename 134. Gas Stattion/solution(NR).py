class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        else:
            f = -1
            n = len(gas)
            for i in range(n):
                fuel = 0
                for j in range(n):
                    pos = (i+j)%n
                    fuel += gas[pos] - cost[pos]
                    if fuel<0:
                        break
                if fuel>=0:
                    f = i
                    break
            return f
                    
