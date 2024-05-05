class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        
        f = defaultdict(int)
        for i in range(0,n,k):
            s = word[i:k+i]
            f[s]+=1
            
        c = max(f, key = f.get)
        
        ans = 0
        for k in f:
            if k!=c:
                ans+=f[k]
                
        return ans
        
        
