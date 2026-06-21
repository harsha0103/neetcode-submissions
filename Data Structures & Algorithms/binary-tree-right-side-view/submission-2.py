# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        if not root:
            return []
        
        def dfs(node):
            if not node :
                return None 
            
            if not node.left and not node.right:
                return [node.val]

            left=dfs(node.left)
            right=dfs(node.right)
            if right:
                right.append(node.val)
                return right
            
        
        return dfs(root)[::-1]
            