class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            pr=(mid-1+len(nums))%len(nums)
            nxt=(mid+1)%len(nums)

            if nums[pr]>=nums[mid] and nums[mid]<=nums[nxt]:
                    return nums[mid]
            elif nums[mid]<nums[l]:
                    r=mid-1
            else:
                l=mid+1
