class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d={}
        def dfs(i):

            if i>=len(nums):
                return 0

            if i in d:
                return d[i] 
            temp=dfs(i+1)
            if i+1<len(nums) and nums[i+1]>nums[i]:
                temp=max(temp,1+dfs(i+1))
            
                
            print(temp,nums[i])
        
            d[i]=temp
            return temp
        return dfs(0)+1