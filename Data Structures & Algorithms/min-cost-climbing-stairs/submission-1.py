class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d={}
        def dfs(i):
            if i>=len(cost):
                return 0
            
            if i in d:
                return d[i]

            mn= cost[i]+min(dfs(i+1),dfs(i+2))
            d[i]=mn

            return mn
        
        return min(dfs(0),dfs(1))
        