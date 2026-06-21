class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp={}
        def count(r,c,row,col):
            if r==row or c==col:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            if r==row-1 and c==col-1:
                return 1
            if obstacleGrid[r][c]==1:
                dp[(r,c)]=0
                return 0
            dp[(r,c)]=count(r+1,c,row,col)+count(r,c+1,row,col)
            return dp[(r,c)]
    
        return count(0,0,len(obstacleGrid),len(obstacleGrid[0]))