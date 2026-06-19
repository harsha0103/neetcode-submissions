# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res1=self.dfs(root,p)
        res2=self.dfs(root,q)
        res1.reverse()
        res2.reverse()
        res=None

        for i,j in  zip(res1,res2):
            if i!=j:
                return res
            res=i

        return res 

    def dfs(self,root,node):

        if not root:
            return None
        
        if root.val==node.val:
            return [root]

        left = self.dfs(root.left,node)
        if left:
            left.append(root)
            return left
        right= self.dfs(root.right,node)
        if right:
            right.append(root)
            return right

        return None