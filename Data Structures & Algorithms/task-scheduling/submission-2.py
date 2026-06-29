from collections import deque,defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d=defaultdict(int)

        for t in tasks:
            d[t]-=1
        max_heap=[]

        for i in d:
            heapq.heappush(max_heap,d[i])

        q=deque()
        runtime=0
        while q or max_heap:
            runtime+=1
            if len(max_heap)>0:
                freq=heapq.heappop(max_heap)
                freq+=1
                if freq:
                    q.append((freq,runtime+n))
            
            if q and q[0][1]==runtime:
                freq,time=q.popleft()
                heapq.heappush(max_heap,freq)
        return runtime
        

