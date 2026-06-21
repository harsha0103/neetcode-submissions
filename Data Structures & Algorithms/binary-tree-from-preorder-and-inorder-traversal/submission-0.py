# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        value=preorder[0]
        root=TreeNode(value)

        mid= inorder.index(value)
        inorder_left=inorder[:mid]
        inorder_right=inorder[mid+1:]

        preorder_left=preorder[1:len(inorder_left)+1]
        preorder_right=preorder[len(inorder_left)+1:]

        root.left=self.buildTree(preorder_left,inorder_left)
        root.right=self.buildTree(inorder_right,preorder_right)

        return root



