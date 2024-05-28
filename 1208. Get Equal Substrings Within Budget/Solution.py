class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        ans = 0
        window = 0
        left = 0
        
        for right in range(n):
            window += abs(ord(s[right]) - ord(t[right]))
            while window > maxCost:
                window -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
