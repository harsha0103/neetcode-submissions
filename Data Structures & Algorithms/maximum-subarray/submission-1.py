class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max=nums[0]
        res=nums[0]

        for num in nums[1:]:
            global_max= max(num,global_max+num)
            res= max(res,global_max)
        
        return res
        