class Solution:
    def findMin(self, a: List[int]) -> int:
        beg=0
        last=len(a)-1
        while beg<last:
            mid=(last+beg)//2
            if a[mid]>a[last]:
                beg=mid+1
            elif a[mid]<a[last]:
                last=mid
            else:
                last-=1
        return a[beg]
