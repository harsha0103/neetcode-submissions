class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d={}
        def dfs(i,j):

            if i>=len(nums):
                return 0

            if i in d:
                return d[i] 
            temp=dfs(i+1,j)
            if j==-1 or  nums[i]>nums[j]:
                temp=max(temp,1+dfs(i+1,i))
                
            print(temp,nums[i])
        
            d[i]=temp
            return temp
        return dfs(0,-1)+1