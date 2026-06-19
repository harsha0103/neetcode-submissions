class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]


        for i in range(len(intervals)):
            x1,y1=res.pop()
            x2,y2=intervals[i]

            if x1>y2:
                res.append(intervals[i])
                res.append([x1,y1])

            
            elif x2>y1:
                res.append([x1,y1])
                res.append(intervals[i])

            
            else:
                x1=min(x1,x2)
                y1=max(y1,y2)
                res.append([x1,y1])
        
        return res
