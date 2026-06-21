class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums=[0]+nums
        total=0
        k_count=0
        for i in range(len(nums)):
            total+=nums[i]
            nums[i]=total
            if nums[i]==k or total==k:
                k_count+=1
        
        for i in range(len(nums)-1):
            if nums[len(nums)-1]-nums[i]==k:
                k_count+=1
        
        return k_count
