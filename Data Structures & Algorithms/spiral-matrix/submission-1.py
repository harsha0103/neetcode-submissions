class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row,col=len(matrix),len(matrix[0])
        res=[]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c,visited,d):
            
            if len(res)==row*col:
                return 

            visited.add((r,c))
            res.append(matrix[r][c])
            
            dr,dc=direction[d]
            nr=r+dr
            nc=c+dc
            v_r= 0<= nr<row
            v_c= 0<= nc< col

            if v_c and v_r and (nr,nc) not in visited:
                dfs(nr,nc,visited,d)
            else:
                d=(d+1)%4
                dr,dc=direction[d]
                nr=r+dr
                nc=c+dc
                v_r= 0<= nr<row
                v_c= 0<= nc< col

                if v_c and v_r and (nr,nc) not in visited:
                    dfs(nr,nc,visited,d)
        dfs(0,0,set(),0)
        return res