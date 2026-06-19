class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max=nums[0]
        global_min=nums[0]
        res_max=nums[0]
        res_min=nums[0]

        for num in nums[1:]:
            temp_max=max(num,global_max+num,global_min+num)
            temp_min=min(num,global_max+num,global_min+num)
            global_max=temp_max
            global_min=temp_min

            res_max= max(global_max,res_max)
            res_min= min(global_min,res_min)
        
        res=max(res_max, sum(nums)-res_min) 

        return res if res!=0 else max(nums)