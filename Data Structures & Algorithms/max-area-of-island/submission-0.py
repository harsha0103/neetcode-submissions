class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visited=set()
        max_area=0
        for r in range(row):
            for c in range(col):
                area=self.dfs(grid,r,c,visited)
                print(area)
                max_area=max(area,max_area)
        return max_area

    def dfs(self,grid,r,c,visited):
        valid_r= 0<= r<len(grid)
        valid_c= 0<= c< len(grid[0])

        if not valid_r or not valid_c:
            return 0
        
        if (r,c) in visited:
            return 0
        visited.add((r,c))

        if grid[r][c]==0:
            return 0
        
        area=1
        area+=self.dfs(grid,r+1,c,visited)
        area+=self.dfs(grid,r-1,c,visited)
        area+=self.dfs(grid,r,c+1,visited)
        area+=self.dfs(grid,r,c-1,visited)

        return area  