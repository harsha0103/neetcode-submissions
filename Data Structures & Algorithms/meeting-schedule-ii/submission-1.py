"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        count=0
        intervals.sort(key=lambda i:i.end)
        prev=intervals[0].end
        for i in intervals[1:]:
            if i.start<prev:
                count+=1
            
            else:
                prev=i.end
        
        return len(intervals)-count