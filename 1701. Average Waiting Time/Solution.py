class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        time = customers[0][0]
        n = len(customers)
        for i in range(n):
            if time >= customers[i][0]:
                time += customers[i][1]
                total_time += time - customers[i][0]
            else: 
                total_time += customers[i][1]
                time = customers[i][0] + customers[i][1]
            
        return total_time/n
