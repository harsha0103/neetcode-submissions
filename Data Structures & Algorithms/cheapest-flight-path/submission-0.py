from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph=defaultdict(list)

        for source,target,cost in flights:
            graph[source].append((target,cost))
        min_heap=[(0,src,-1)]

        while min_heap:
            cost, dest,stops=heapq.heappop(min_heap)
            print(cost,dest,stops)
            
            if dest==dst:
                print(dest)
                if k>=stops:
                    return cost
 
            if stops>k:
                continue
            
            for next_stop,inc_cost in graph[dest]:
                heapq.heappush(min_heap,(inc_cost+cost,next_stop,stops+1))
        return -1

            