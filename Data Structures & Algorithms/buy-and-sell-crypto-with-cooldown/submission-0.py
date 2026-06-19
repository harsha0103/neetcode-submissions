class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Buy -> i+1
        #sell -> i+2 cos fo cooldown
        dp={}
        def dfs(i,buying):
            if i >=len(prices):
                return 0
            total=float('-inf')
            if (i,buying) in dp:
                return dp[(i,buying)]
            if buying:
                buy=dfs(i+1,not buying)-prices[i]
                cooldown= dfs(i+1,buying)
                total=max(total,buy,cooldown)
            else:
                sell=dfs(i+2,not buying)+prices[i]
                cooldown= dfs(i+1,buying)
                total=max(total,sell,cooldown)
            dp[(i,buying)]=total

            return total
        return dfs(0,True)
