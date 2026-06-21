class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_val=set()

        l=0
        res=[]

        for r in range(len(nums)):
            if (r-l+1 >k):
                res.append(max(max_val))
                max_val.discard(nums[l])
                l+=1
            

            max_val.add(nums[r])
        res.append(max(max_val))
        return res