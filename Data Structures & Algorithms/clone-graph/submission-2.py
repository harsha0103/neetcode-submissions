"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new=defaultdict(int)

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            if not node:
                return None
            
            node1=Node(node.val)
            old_to_new[node]=node1
            for nei in node.neighbors:
                node1.neighbors.append(dfs(nei))
            
            return node1
        
        return dfs(node)
        