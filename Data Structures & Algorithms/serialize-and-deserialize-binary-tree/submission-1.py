# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string=[]
        def dfs(root):
            if not root:
                string.append('N')
                return 
            string.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res=','.join(string)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=='N':
            return None
        arr=data.split(',')
        arr=arr[::-1]
        def helper():
            if not arr:
                return None
            
            curr=arr.pop()
            if curr=='N':
                return None
            
            node=TreeNode(curr)
            node.left=helper()
            node.right=helper()

            return node

        return helper()