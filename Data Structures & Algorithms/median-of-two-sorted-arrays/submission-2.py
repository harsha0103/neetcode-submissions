class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b=nums1,nums2
        total=len(nums1)+len(nums2)
        half=total//2

        if len(b)>len(a):
            a,b=b,a

        l,r=0,len(a)-1

        while True:
            mid_a=(l+r)//2 #mid for a
            mid_b= half-mid-2

            aleft= a[mid_a] if mid_a>=0 else float('-inf')
            aright=a[mid_a+1] if mid_a<len(a) else float('inf')
            bleft=b[mid_b] if mid_b>=0 else float('-inf')
            bright=b[mid_b] if mid_b<len(b) else float('-inf')

            if aleft<=bright and bleft<=aright:
                #odd
                if total%2:
                    return min(bright,aright)
                else:
                   return  max(aleft,bleft)+min(aright,bright)//2
            
            elif aleft>bright:
                r=mid_a-1
            else:
                l=mid_a+1