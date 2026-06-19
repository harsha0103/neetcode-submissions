class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp={}
        def dfs(i,j):
            if i>=j:
                return 0
            mr=float('-inf')
            if (i,j) in dp:
                return dp[(i,j)]

            for k in range(i,j):
                res=dfs(i,k)+dfs(k+1,j)+nums[i-1]*nums[k]*nums[j]
                mr=max(res,mr)
            dp[(i,j)]=mr
            return mr
        
        return dfs(1,n-1)