from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        q=deque()
        fresh_fruit=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c,0))
                if grid[r][c]==1:
                    fresh_fruit+=1
        visited=set()
        max_dist=0
        while q:
            curr_row,curr_col,dist=q.popleft()
            max_dist=max(max_dist,dist)
            deltas=[(1,0),(0,1),(-1,0),(0,-1)]
            for x,y in deltas:
                new_row=curr_row+x
                new_col=curr_col+y

                valid_row= 0<= new_row<row
                valid_col= 0<= new_col<col

                if (valid_row and valid_col and (new_row,new_col) 
                    not in visited and grid[new_row][new_col]==1):
                    visited.add((new_row,new_col))
                    q.append((new_row,new_col,dist+1))
                    fresh_fruit-=1
        
        return max_dist if fresh_fruit==0 else -1


