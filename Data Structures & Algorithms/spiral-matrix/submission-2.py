class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        deltas=[(0,1),(1,0),(0,-1),(-1,0)]
        visited=set()
        res=[]
        row,col=len(matrix),len(matrix[0])
        def dfs(r,c,d):
            visited.add((r,c))
            res.append(matrix[r][c])
            dr,dc=deltas[d]
            nr,nc=r+dr,c+dc

            if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited:
                dfs(nr,nc,d)
            
            else:
                d=(d+1)%4
                dr,dc=deltas[d]
                nr,nc=r+dr,c+dc
                if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited:
                    dfs(nr,nc,d)
        dfs(0,0,0)
        return res
