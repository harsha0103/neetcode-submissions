class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        m=sum(stones)//2
        n=len(stones)

        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            for j in range(m+1):
                if j==0:
                    dp[i][j]=True
                if stones[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j-stones[i-1]] or dp[i-1][j]
        
        subset1=0
        for j in range(m+1):
            if dp[n][j]:
                subset1=j
      
        
        print(dp)

        return abs(2*(subset1)-sum(stones))
