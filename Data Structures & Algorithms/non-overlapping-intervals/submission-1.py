class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last_val=intervals[0][1]
        counter=0
        for x,y in intervals[1:]:
            if last_val>x:
                counter+=1
            else:
                last_val=y
        return counter