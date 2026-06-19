class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap=[]
        for index in range(1,len(points)):
            distance=abs(points[index][0]-points[0][0])+ abs(points[index][1]-points[0][1])
            heapq.heappush(min_heap,(distance,index))

        acc_cost=[]
        visited=set()

        visited.add(0)
        while min_heap:
            cost,dest_index=heapq.heappop(min_heap)
            if dest_index in visited:
                continue
            
            acc_cost.append(cost)
            visited.add(dest_index)
            for i in range(len(points)):
                if i not in visited:
                    distance=(abs(points[i][0]-points[dest_index][0])+ 
                                abs(points[i][1]-points[dest_index][1]))
                    heapq.heappush(min_heap,(distance,i))
        
        return sum(acc_cost)