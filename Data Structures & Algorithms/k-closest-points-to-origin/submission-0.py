from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        my_heap=[]
        for point in points:
            x,y=point
            dist=sqrt(x*x+y*y)
            heapq.heappush(my_heap,(-dist,x,y))
            while len(my_heap)>k:
                heapq.heappop(my_heap)
            
        res=[]
        while my_heap:
            dist,x,y=heapq.heappop(my_heap)
            res.append([x,y])
        return res