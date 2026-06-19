class Solution:
    def climbStairs(self, n: int) -> int:
        d={}
        def dfs(i):
            if i ==n:
                return 1
            
            if i in d:
                return d[i]
            if i>n:
                return 0
            
            mn=dfs(i+1)+dfs(i+2)
            d[i]=mn

            return mn
        
        return dfs(0)