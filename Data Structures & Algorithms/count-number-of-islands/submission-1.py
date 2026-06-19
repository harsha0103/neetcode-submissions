class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs(grid,i,j,visited):
                    count+=1
        
        return count


    def dfs(self,grid,row,col,visited):
        row_valid= 0<= row<len(grid)
        col_valid= 0<= col<len(grid[0])

        if not row_valid or not col_valid or (row,col) in visited:
            return False
        
        visited.add((row,col))
        if grid[row][col]=='0':
            return False
        
        
        
        self.dfs(grid,row+1,col,visited)
        self.dfs(grid,row-1,col,visited)
        self.dfs(grid,row,col+1,visited)
        self.dfs(grid,row,col-1,visited)

        return True