# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l=1
        if root:
            q=deque([root])
        else:
            return []
        res=[]

        while q:
            if l==0:
                l=len(q)
            l-=1
            current=q.popleft()
            if l==0:
                res.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        return res
        
        