# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        borrow=0
        res= ListNode(0)
        res1=res
        while l1 or l2:
            if l1 and l2:
                s=l1.val+l2.val+borrow
                l1=l1.next
                l2=l2.next
            elif l1:
                s=l1.val+borrow
                l1=l1.next
            else:
                s=l2.val+borrow
                l2=l2.next
            borrow=s//10
            res.next=ListNode(s%10)
            res=res.next
        if borrow==1:
            res.next=ListNode(1)

        return res1.next


