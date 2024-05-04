class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = (sum(aliceSizes)-sum(bobSizes)) // 2
        aliceSizes = set(aliceSizes)
        for s in set(bobSizes):
            if a + s in aliceSizes:
                return [a+s, s]
