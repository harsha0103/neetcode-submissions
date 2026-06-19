"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start= [ i.start for i in intervals]
        end= [ i.end for i in intervals ]
        start.sort()
        end.sort()
        count =0
        max_count=0
        i,j=0,0
        while i< len(intervals): 
            if start[i]<end[j]:
                count+=1
                i+=1
            else:
                j+=1
                count-=1
            max_count=max(count,max_count)
        return max_count