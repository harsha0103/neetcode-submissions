# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque([root]) if root else []
        temp=[]
        res=[]
        l=1
        while q:
            if l==0:
                res.append(temp[-1])
                temp=[]
                l=len(q)

            l-=1
            curr=q.popleft()
            temp.append(curr.val)
            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)
            
        if len(temp)>0:
            res.append(temp[-1])
        
        return res