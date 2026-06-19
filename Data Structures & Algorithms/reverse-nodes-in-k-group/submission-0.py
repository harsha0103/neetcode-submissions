# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)
        groupprev=dummy
        
        while True:

            kth=self.group(groupprev,k)
            if not kth:
                break

            groupnext=kth.next

            self.reverse(groupprev.next,kth.next,groupnext)

            temp=groupprev.next
            groupprev.next=kth
            groupprev=temp
        return dummy.next
    
    def group(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr


    def reverse(self,head,prev,groupnext):
        if head==groupnext:
            return prev 
        
        new=head.next
        head.next=prev
        return self.reverse(new,head,groupnext)