class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_val=0

        l=0
        res=[]

        for r in range(len(nums)):
            if (r-l+1 >k):
                res.append(max_val)
                l+=1

            max_val=max(max_val,nums[r])
        res.append(max_val)
        return res