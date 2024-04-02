class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            # we are updating the count value in dictionary and if it does not exist we are making it 1 in dictionary count.
            count[s[r]] = 1 + count.get(s[r], 0)

            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
