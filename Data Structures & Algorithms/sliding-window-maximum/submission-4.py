from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque([])

        l=0
        res=[]

        for r in range(len(nums)):
            if (r-l+1 >k):
                res.append(q[0])
                l+=1
            while q and q[-1]<nums[r]:
                q.pop()
            q.append(nums[r])
            nums.append(nums[r])
        res.append(q[0])
        return res