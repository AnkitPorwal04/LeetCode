class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        count = 0
        for i in tasks:
            freq[ord(i) - ord('A')] += 1

        freq.sort()
        chunk = freq[25] - 1
        idle = chunk * n

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)
            
                
