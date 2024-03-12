# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(0, head)
        seen = {0: fake}        
        summ = 0
        while head:
            summ += head.val            
            seen[summ] = head
            head = head.next
        head = fake
        summ = 0
        while head:
            summ += head.val
            head.next = seen[summ].next
            head = head.next
        return fake.next
