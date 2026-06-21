class Solution:
    def rob(self, nums: List[int]) -> int:
        
    
        def dfs(i):
            if i>=len(nums):
                return 0 
            
            res=max(dfs(i+1),nums[i]+dfs(i+2))
            return res
        max_res=0
        i=0
        while i<len(nums):
            print(dfs(i))
            max_res= max(max_res, dfs(i))
            i+=1
        return max_res

            