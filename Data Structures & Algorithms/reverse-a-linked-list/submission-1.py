# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res= None
        res2= head
        while res2:
            head= res2
            res2=res2.next
            head.next=res
            res=head
        return res             