class Solution:
    def trap(self, height: List[int]) -> int:
        prev = []
        ahead = []
        for i in range(len(height)):
            prev.append(max(height[:i+1]))
            ahead.append(max(height[i:]))
        ans = [(min(prev[i],ahead[i])-height[i]) for i in range(len(height))]
        return(sum(ans))
