class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        left = set()
        right = Counter(s)

        for m in s:
            right[m] -= 1
            for c in left:
                if right[c] > 0:
                    ans.add(""+m+c)
            left.add(m)
        return len(ans)
