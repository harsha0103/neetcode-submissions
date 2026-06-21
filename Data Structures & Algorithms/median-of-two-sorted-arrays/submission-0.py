class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total= len(nums1)+len(nums2)
        med=total//2
        i=med//2
        j=med-i
        while nums1[i]>nums2[j+1] and nums2[j]>nums1[i+1]:

            if nums1[i]>nums2[j+1]:
                i-=1
                j+=1
            elif nums2[j]>nums1[i+1]:
                i+=1
                j-=1
        
        if total%2==0:
            res=max (nums1[i],nums2[j]) + min(nums1[i+1],nums2[j+1])
            return res/2
        else:
            res=min (nums1[i+1],nums2[j+1])
            return res


