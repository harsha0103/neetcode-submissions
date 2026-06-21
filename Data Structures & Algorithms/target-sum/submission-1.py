class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m=(sum(nums)+target)//2
        n=len(nums)

        s1=(sum(nums)-target)//2
        s2=(sum(nums)+target)//2

        if s1+s2!= sum(nums):
            return 0
        
        dp=[[0]*(m+1) for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(m+1):
                if j==0:
                    dp[i][j]=1
                if j>nums[i-1]:
                    dp[i][j]=dp[i-1][j]

                else:
                    dp[i][j]= dp[i-1][j]+dp[i-1][j-nums[i-1]]            
        
        return dp[n][m]