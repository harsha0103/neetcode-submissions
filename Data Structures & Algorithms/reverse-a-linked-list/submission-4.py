# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        

        def helper(head,prev):
            if not head:
                return prev
            new=head.next
            head.next=prev
            return helper(new,head)
        
        new=helper(head,None)
        return new