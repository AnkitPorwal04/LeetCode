# Ctreative solution

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n2 = len(arr2)
        a2i=[n2]*1001

        for i, x in enumerate(arr2):
            a2i[x]=i
        
        arr1.sort(key=lambda x: (a2i[x], x))

        return arr1
        
        
