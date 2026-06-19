class MedianFinder:

    def __init__(self):
        self.first_heap=[]
        self.second_heap=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_heap,num*-1)
        if len(self.first_heap)>len(self.second_heap):
            temp=heapq.heappop(self.first_heap) 
            heapq.heappush(self.second_heap,temp*-1)
        if len(self.second_heap)> len(self.first_heap):
            temp=heapq.heappop(self.second_heap) 
            heapq.heappush(self.first_heap,temp*-1)

    def findMedian(self) -> float:
        if len(self.first_heap)>len(self.second_heap):
            return self.first_heap[0]*-1
        elif len(self.first_heap)<len(self.second_heap):
            return self.second_heap[0]
        else:
            avg=float(self.first_heap[0]*-1 +  self.second_heap[0])/2
            return avg
        
        