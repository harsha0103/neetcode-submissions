class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max=nums[0]
        res_max=nums[0]

        for i in nums[1:]:
            temp_max=max(i,global_max+i)
            global_max=temp_max
            

            res_max=max(global_max,res_max)
        
        
        
        return res_max

        