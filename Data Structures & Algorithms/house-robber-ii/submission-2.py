class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def dfs(arr):
            rob1,rob2=0,0

            for i in arr:
                temp=max(rob1+i,rob2)
                rob1=rob2
                rob2=temp
            
            return rob2
        
        return max(dfs(nums[1:]),dfs(nums[:-1]))