class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        new_nums=[0]+nums
        total=0
        k_count=0
        for i in range(len(nums)+1):
            total+=new_nums[i]
            new_nums[i]=total
            if i<len(nums) and nums[i]==k:
                k_count+=1
            if total==k:
                k_count+=1
        
        for i in range(len(nums)-1):
            if nums[len(nums)-1]-nums[i]==k:
                k_count+=1
        
        return k_count
