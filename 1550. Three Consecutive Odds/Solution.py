class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n-2):
            if (arr[i] % 2) != 0 and (arr[i+1]) % 2 != 0 and (arr[i+2]) % 2 != 0:
                return True
        return False
