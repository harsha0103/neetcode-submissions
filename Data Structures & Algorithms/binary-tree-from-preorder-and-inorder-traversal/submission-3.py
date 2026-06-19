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
        node=TreeNode(value)


        mid=inorder.index(value)
        right_inorder=inorder[mid+1:]
        left_inorder=inorder[:mid]
        left_preorder=preorder[1:len(left_inorder)+1]
        right_preorder=preorder[len(left_inorder)+1:]

        node.left=self.buildTree(left_preorder,left_inorder)
        node.right=self.buildTree(right_preorder,right_inorder)

        return node