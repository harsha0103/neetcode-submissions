class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        pre=1
        for i in range(len(nums)):
            prefix.append(pre)
            pre*=nums[i]
        post=1
        print(prefix)
        for i in range(len(nums)-1,-1,-1):
            prefix[i]*=post
            post*=nums[i]
        return prefix