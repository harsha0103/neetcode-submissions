# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            stack=[(root,0)] 
        else:
             return 0
        mdepth=float('-inf')
        while stack:
            current,d= stack.pop()
            
            if current.left:
                stack.append((current.left,d+1))
            if current.right:
                stack.append((current.right,d+1))
            
            if current.left is None and current.right is None:
                mdepth=max(mdepth,d)
        return mdepth+1

        