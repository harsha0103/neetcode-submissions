class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap=[]

        for num in nums:
            heapq.heappush(my_heap,num)
        k1=len(nums)-k

        while k1>0:
            heapq.heappop(my_heap)
            k1-=1
        return heapq.heappop(my_heap)