class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0, 1
        res = []

        while left <= right:
            mid = left + (right - left) / 2
            j, total, num, den = 1, 0, 0, 0
            maxFrac = 0
            for i in range(n):
                while j < n and arr[i] > arr[j] * mid:
                    j += 1
                
                total += n - j

                if j < n and maxFrac < arr[i] * 1.0 / arr[j]:
                    maxFrac = arr[i] * 1.0 / arr[j]
                    num, den = i, j

            if total == k:
                res = [arr[num], arr[den]]
                break

            if total > k:
                right = mid
            else:
                left = mid

        return res
