class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1=[0]
        cost1.extend(cost)
        d={}

        def dp(i):
            if i >= len(cost1):
                return 0
             
            if i in d:
                return d[i]

            d[i]=cost1[i]+min(dp(i+1), dp(i+2))
            return d[i]        
        return dp(0)