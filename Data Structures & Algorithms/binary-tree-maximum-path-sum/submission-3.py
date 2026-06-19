# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_val=float('-inf')
        def dfs(root):
            if not root:
                return 0

            left =dfs(root.left)
            right=dfs(root.right)

            left_max=max(left,0)
            right_max=max(right,0)


            self.max_val=max(self.max_val,root.val+left_max+right_max)
            return max(root.val,root.val+max(left,right))
        dfs(root)

        return self.max_val