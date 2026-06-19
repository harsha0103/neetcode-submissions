from collections import defaultdict,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        my_heap=[]
        #get the frequency
        d=defaultdict(int)
        for task in tasks:
            d[task]+=1
        
        
        #get the heapify
        for i in d:
            heapq.heappush(my_heap,-d[i])
        

        #run the loop until the heap is empty 
        run_time=0
        q=deque()
        while my_heap or q:
            
            run_time+=1
            if my_heap:
                freq=heapq.heappop(my_heap)
                freq+=1
                if freq:
                    q.append((freq,run_time+n))

            if q and q[0][1]==run_time:
                freq,time=q.popleft()
                heapq.heappush(my_heap,freq)

        return run_time