# Not so good solution

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res1 = []
        res2 = []
        for i in arr2:
            n = arr1.count(i)
            if n > 0:
                for j in range(n):
                    res1.append(i)
                    arr1.remove(i)
        arr1.sort()
        return res1 + arr1
