class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if nums[l]<nums[r]:
            return nums[l]
        n=len(nums)
        while l<=r:
            mid=(l+r)//2
            pr=(mid-1+n)%n
            nr=(mid+1)%n
            if  nums[mid]<=nums[pr] and  nums[mid]<=nums[nr]:
                return nums[mid]

            elif nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1
        
        return-1
