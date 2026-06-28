import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        final=[]
        for i in points:
            x1,y1=i
            dist=math.sqrt(x1*x1 + y1*y1)
            heapq.heappush(res,(dist,i))


        while k>0:
            k-=1
            i,j=heapq.heappop(res)
            final.append(j)

        return final

