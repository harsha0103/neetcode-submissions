class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        my_heap=[]
        for weight in stones:
            heapq.heappush(my_heap,(-weight,weight))
    
        while len(my_heap)>1:
            weight1=heapq.heappop(my_heap)[1]
            weight2=heapq.heappop(my_heap)[1]
            diff=weight1-weight2
            heapq.heappush(my_heap,(-diff,diff))
        
        return my_heap.pop()[1]
        