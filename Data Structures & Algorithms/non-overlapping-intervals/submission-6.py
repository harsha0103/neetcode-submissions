class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])
        print(intervals)
        p=intervals[0][1]
        count=0

        for i,j in intervals[1:]:
    
            if p>i:

                count+=1               
            else:
                p=j
        
        return count