# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=slow.next
        slow.next=None
        second=None
        while prev:
            new=prev.next
            prev.next=second
            second=prev
            prev=new
        
        first=head

        while second:
            temp1,temp2=first.next,second.next
            first.next=second
            first=first.next
            first.next=temp1
            first=first.next
            second=temp2