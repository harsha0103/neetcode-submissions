# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            mergedLists=[]
            for i in range (0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                mergedLists.append(self.mergingList(l1,l2))
            lists=mergedLists

        return lists[0]

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
