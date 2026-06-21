class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                continue
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1

        return res