class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        return sum(h1 != h2 for h1, h2 in zip(heights, expected))
