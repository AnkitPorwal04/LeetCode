# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        i, sz, p0, p, minD= 1, 0, -1, -1, 2**31
        x0, x1= head.val, head.next.val
        less, bigger= x1<x0, x1>x0
        Next=head.next.next
        while Next:
            x=Next.val
            bigger1, less1=x>x1, x<x1
            if (less and bigger1) or (bigger and less1):
                if sz==0: p0=i
                sz+=1
                if p!=-1: minD=min(minD, i-p)
                p=i
            bigger, less=bigger1, less1
            x1=x
            i+=1
            Next=Next.next
        if sz<=1: return [-1,-1]
        else: return [minD, p-p0]
        
