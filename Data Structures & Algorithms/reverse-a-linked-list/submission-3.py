# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.helper(head,None)

    def helper(self,head,prev):
        if not head:
            return prev
        new=head.next
        head.next=prev
        return self.helper(new,head)