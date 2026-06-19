import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for x,y,t in times:
            graph[x].append((y,t))

        min_heap=[(0,k)]
        res={}
        total_time=0
        while min_heap:
            time,node=heapq.heappop(min_heap)
            if node in res:
                continue
            total_time =time
            res[node]=time
            for neighbor,new_time in graph[node]:
                if neighbor not in res:
                    heapq.heappush(min_heap,(time+new_time,neighbor))
        return total_time if len(res)==n else -1
             

        