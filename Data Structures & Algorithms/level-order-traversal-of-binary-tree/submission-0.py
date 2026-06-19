# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root:
            q=deque([root]) 
        else:
            return []
        l=1
        tres=[]

        while q:
            if l==0:
              l=len(q)
              res.append(tres)
              tres=[]
            l-=1
            current=q.popleft()
            tres.append(current.val)
        
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        res.append(tres)
        return res



        