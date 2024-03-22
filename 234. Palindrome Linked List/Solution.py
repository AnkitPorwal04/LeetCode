# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s1 = ''
        curr = head
        while curr:
            s1 = s1 + str(curr.val)
            curr = curr.next
        
        if s1 == s1[::-1]:
            return True
        else:
            return False
