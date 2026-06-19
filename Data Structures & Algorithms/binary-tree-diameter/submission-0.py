# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Recursive 
        self.m=0
        self.dia(root)
        return self.m
    def dia(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        
        left=self.dia(root.left)
        right=self.dia(root.right)
        self.m=max(self.m,left+right)

        return 1+max(left,right)

        