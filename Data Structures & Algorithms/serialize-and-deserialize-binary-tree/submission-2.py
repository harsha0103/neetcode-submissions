# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr=[]
        def dfs(root):
            if not root:
                arr.append('NA')
                return 
            
            arr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

            return arr
        dfs(root)
        return ','.join(arr)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=='NA':
            return None 

        arr=data.split(',')
        arr.reverse()

        def helper():
            if len(arr)==0:
                return None
            
            curr=arr.pop()
            if curr=='NA':
                return None
            
            node=TreeNode(curr)
            node.left=helper()
            node.right=helper()

            return node
        
        return helper()
