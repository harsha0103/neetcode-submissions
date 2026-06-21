class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d={}
        def dfs(i):

            if i>=len(nums):
                return 0

            if i in d:
                return d[i] 
            count=0
            if i+1<len(nums) and nums[i+1]>nums[i]:
                temp=1+dfs(i+1)
            else:
                temp=dfs(i+1)
            
            count=max(temp,count)
            d[i]=count
            return count
        return dfs(0)+1