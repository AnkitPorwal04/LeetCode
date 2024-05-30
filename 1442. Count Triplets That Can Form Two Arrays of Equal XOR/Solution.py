class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        for i in range(n-1):
            a = 0
            for j in range(i+1, n):
                a ^= arr[j-1]
                b = 0
                for k in range(j, n):
                    b ^= arr[k]
                    if a == b:
                        res += 1
        return res
                    
