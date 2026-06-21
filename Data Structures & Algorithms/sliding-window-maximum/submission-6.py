from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque([])

        l=r=0
        res=[]

        while r < len(nums):
            while q and q[-1]<nums[r]:
                q.pop()
            q.append(nums[r])
            if q[0]<nums[l]:
                q.popleft()
            if (r-l+1 >=k):
                res.append(q[0])
                l+=1
            
            r+=1
            
        return res