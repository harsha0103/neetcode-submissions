class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d={}
        def dfs(i,j):

            if i==len(nums):
                return 0
            if (i,j) in d:
                return d[(i,j)]
            not_take=dfs(i+1,j)
            take=0
            if j==-1 or  nums[i]>nums[j]:
                take=1+dfs(i+1,i)
            
            
            res=max(take,not_take)
            d[(i,j)]=res

            return res
        return dfs(0,-1)