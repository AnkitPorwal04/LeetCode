class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n, flipped, res = len(A), 0, 0
        fp = [0] * n
        for i in range(n):
            if i >= K:
                flipped ^= fp[i - K]
            if flipped == A[i]:
                if i + K > n:
                    return -1
                fp[i] = 1
                flipped ^= 1
                res += 1
        return res
