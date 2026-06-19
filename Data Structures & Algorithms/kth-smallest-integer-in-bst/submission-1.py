# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited=self.inorder(root,[])
        return visited[k-1]
        
        
    def inorder(self,root,visited):
        if not root:
            return None
        
        self.inorder(root.left,visited)
        visited.append(root.val)
        self.inorder(root.right,visited)
        return visited