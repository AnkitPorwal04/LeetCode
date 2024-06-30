class Solution:

    def dfs(self,vis,li,com,i):
        if(vis[i]):
            return 0
        vis[i]=com
        ans=1
        for j in li[i]:
            ans+=self.dfs(vis,li,com,j)
        return ans

    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        ans=0
        li=[[] for i in range(n)]
        for l in e:
            if(l[0]==3):
                li[l[1]-1].append(l[2]-1)
                li[l[2]-1].append(l[1]-1)
        vis=[0 for i in range(n)]
        com=0
        for i in range(n):
            if(vis[i]):
                continue
            else:
                com+=1
                temp=self.dfs(vis,li,com,i)
                ans+=(temp-1)
        lia=[[] for i in range(com)]
        lib=[[] for i in range(com)]
        for l in e:
            if(l[0]==1):
                a=vis[l[1]-1]-1
                b=vis[l[2]-1]-1
                if(a==b):
                    continue
                lia[a].append(b)
                lia[b].append(a)
            elif(l[0]==2):
                a=vis[l[1]-1]-1
                b=vis[l[2]-1]-1
                if(a==b):
                    continue
                lib[a].append(b)
                lib[b].append(a)
        visa=[0 for i in range(com)]
        coma=0
        comb=0
        for i in range(com):
            if(visa[i]):
                continue
            else:
                coma+=1
                if(coma>1):
                    return -1
                self.dfs(visa,lia,coma,i)
        
        visb=[0 for i in range(com)]
        for i in range(com):
            if(visb[i]):
                continue
            else:
                comb+=1
                if(comb>1):
                    return -1
                self.dfs(visb,lib,comb,i)
        if(coma>1 or comb>1):
            return -1
        ans+=(com-1)*2
        return len(e)-ans
