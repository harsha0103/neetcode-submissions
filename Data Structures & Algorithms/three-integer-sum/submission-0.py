class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i,val in enumerate(nums):
            if i >0 and val==nums[i-1]:
                continue 
            
            left,right=i+1,len(nums)-1

            while left<right :
          
                if nums[left]+nums[right]>-val:
                    right-=1
                elif nums[right]+nums[left]<-val:
                    left+=1
                elif nums[right]+nums[left]==-val:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return res