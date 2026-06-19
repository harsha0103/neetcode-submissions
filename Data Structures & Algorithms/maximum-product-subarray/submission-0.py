class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        global_max=nums[0]
        global_min=nums[0]
        res_max=nums[0]

        for num in nums[1:]:
            temp_max=max(num,global_max*num,global_min*num)
            temp_min=min(num,global_max*num,global_min*num)
            global_min=temp_min
            global_max=temp_max

            res_max=max(res_max,global_max)
        return res_max

