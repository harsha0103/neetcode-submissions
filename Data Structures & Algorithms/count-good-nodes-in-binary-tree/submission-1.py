# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q=deque([(root,root.val)]) if root else []
        count=0
        while q:
            curr,curr_max=q.popleft()

            if curr_max<=curr.val:
                count+=1
                curr_max=max(curr_max,curr.val)
            
            if curr.left:
                q.append((curr.left,curr_max))
            
            if curr.right:
                q.append((curr.right,curr_max))
        return count