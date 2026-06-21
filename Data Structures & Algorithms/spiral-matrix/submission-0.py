class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row,col=len(matrix),len(matrix[0])
        res=[]

        def dfs(r,c,visited):
            v_r= 0<= r<row
            v_c= 0<= c< col

            if not v_c or not v_r or (r,c) in visited:
                return 
            
            visited.add((r,c))
            res.append(matrix[r][c])

            dfs(r,c+1,visited)
            dfs(r+1,c,visited)
            dfs(r,c-1,visited)
            dfs(r-1,c,visited)

        dfs(0,0,set())
        return res