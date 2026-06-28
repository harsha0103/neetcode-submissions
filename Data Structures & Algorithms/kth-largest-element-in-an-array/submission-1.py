import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        final_nums=[-n for n in nums]
        res=0    
        heapq.heapify(final_nums)
        while k>0:
            res=-heapq.heappop(final_nums)
            k-=1
        
        return res
