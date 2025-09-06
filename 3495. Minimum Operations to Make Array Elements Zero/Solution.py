class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for q in queries:
            l = q[0]; r = q[1]; s = 0; op = 0
            rage = 1
            while rage<=r:
                sr = max(l, rage)
                er = min(r, rage*4-1)

                s += max(0, (op+1)*(er-sr+1))
                rage *= 4
                op+=1

            res += (s+1)//2
        return res
