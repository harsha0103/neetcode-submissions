# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
        
        for index in range(len(lists)):
            dummy=self.mergingList(dummy,lists[index])

        return dummy.next

    def mergingList(self,head1,head2):
        dummy=ListNode()
        res=dummy
        while head1 and head2:
            if head1.val<=head2.val:
                res.next=head1
                head1=head1.next
            else:
                res.next=head2
                head2=head2.next
            res=res.next
        if head1:
            res.next=head1
        if head2:
            res.next=head2
        
        return dummy.next
