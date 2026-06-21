class Solution:
    def findMin(self, nums: List[int]) -> int:
        start,end=0,len(nums)-1
        n=len(nums)
        while start<=end:
            mid=start+(end-start)//2
            ne=(mid+1)%n
            pr=(mid-1+n)%n

            if nums[pr]>nums[mid] and nums[mid]<nums[ne]:
                return nums[mid]
            
            if nums[mid]>nums[start]:
                start=mid+1
            else:

                end=mid-1
        return 0


    
        