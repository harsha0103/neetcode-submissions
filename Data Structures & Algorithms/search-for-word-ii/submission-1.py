class TreeNode:
    def __init__(self):
        self.child={}
        self.word=False

    def addword(self,word):
        curr=self
        for c in word:
            if c not in curr.child:
                curr.child[c]=TreeNode()
            curr=curr.child[c]
        curr.word=True
                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TreeNode()
        for word in words:
            root.addword(word)
        
        row,col=len(board),len(board[0])
        res,visited=set(),set()
        def dfs(r,c,node,word):

            r_val= 0<= r<row
            c_val= 0<= c<col
            if (not r_val or not c_val or 
                (r,c) in visited or board[r][c] not in node.child):
                return 
            
            visited.add((r,c))
            node= node.child[board[r][c]]
            word+=board[r][c]

            if node.word:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))

        

        for r in range(row):
            for c in range(col):
                dfs(r,c,root,'')
        
        return list(res)
