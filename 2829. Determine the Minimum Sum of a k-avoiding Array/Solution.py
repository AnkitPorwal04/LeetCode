class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        i = 1
        ans = []
        while len(ans)!=n:
            if k-i not in ans:
                ans.append(i)
            i += 1
        return sum(ans)
