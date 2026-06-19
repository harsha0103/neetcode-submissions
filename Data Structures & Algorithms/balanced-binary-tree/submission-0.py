# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(root: Optional[TreeNode]):    

            if root is None:
                return (True,0)

            lb,lh=check(root.left)
            rb,rh=check(root.right)

            b=lb and rb and abs(lh-rh)<=1

            return (b,1+max(lh,rh))
        b,_=check(root)
        return b
