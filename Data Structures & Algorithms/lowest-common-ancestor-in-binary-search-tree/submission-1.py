# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        arr1=self.dfs(root,p)
        arr2=self.dfs(root,q)
        
        arr1.reverse()
        arr2.reverse()
        res=None
        for i,j in zip(arr1,arr2):
            if i!=j:
                return res
            res=i
        return res

    def dfs(self,root,node):
        if not root:
            return 
        
        if root.val==node.val:
            return [root]
        
        left=self.dfs(root.left,node)
        if left:
            left.append(root)
            return left
        
        right=self.dfs(root.right,node)
        if right:
            right.append(root)
        
            return right
        return None
