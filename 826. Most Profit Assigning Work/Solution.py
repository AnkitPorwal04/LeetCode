class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
            worker.sort()
            jobs=zip(difficulty,profit)
            jobs.sort()
            n=len(jobs)
            best_profit=0
            total_best_profit=0
            i=0
            for s in worker:
                while i<n and s>=jobs[i][0]:
                    best_profit=max(best_profit, jobs[i][1])
                    i+=1
                total_best_profit+=best_profit
            return total_best_profit        
