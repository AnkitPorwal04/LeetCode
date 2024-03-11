class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {}
        ans = ''
        s = list(s)
        s.sort()
        for i in order:
            dic.update({i:order.index(i)})
        lis=[0]*len(s)
        for i in dic.keys():
            if i in s:
                for j in range(s.count(i)):
                    ans += i
        for i in s:
            if i not in ans:
                for j in range(s.count(i)):
                    ans += i
        return ans
        
