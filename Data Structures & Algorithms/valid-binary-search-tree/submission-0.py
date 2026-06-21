# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        visited=self.in_order(root,[])
        return self.is_sorted(visited)
    
    def in_order(self,root,visited):
        if not root :
            return None
        self.in_order(root.left,visited)
        visited.append(root.val)
        self.in_order(root.right,visited)

        return visited
    
    def is_sorted(self,visited):
        for i in  range(1,len(visited)):
            if visited[i-1]>visited[i]:
                return False
        return True

        
