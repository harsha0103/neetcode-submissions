# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root):
            if not root:
                return [True,0]
            
            left,l_h=dfs(root.left)
            right,r_h=dfs(root.right)
        
            curr_bool=left and right and abs(l_h-r_h)<2
            curr_height=1+max(l_h,r_h)

            return [curr_bool,curr_height]
        
        x,y=dfs(root)

        return x