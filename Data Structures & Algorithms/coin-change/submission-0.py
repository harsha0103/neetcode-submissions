class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        m=amount
        dp=[[0]*(m+1) for _ in range(n+1)]
        
        for j in range(m+1):
            dp[0][j]=float('inf')

        for i in range(1,n+1):
            for j in range(1,m+1):
                if coins[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
        
        print(dp)
        return dp[n][m] if dp[n][m]!=float('inf') else -1
