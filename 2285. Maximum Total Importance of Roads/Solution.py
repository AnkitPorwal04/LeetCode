class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees=[0]*n
        for u,v in roads:
            degrees[u]+=1
            degrees[v]+=1
        degrees.sort()
        degrees.reverse()  
        ans=0
        for i,j in enumerate(degrees):
            ans+=(n-i)*j
        return ans     
