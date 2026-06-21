class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=[intervals[0]]
        for x,y in intervals[1:]:
            curr_x,curr_y=res.pop()
            if y<=curr_x:
                res.append([x,y])
                res.append([curr_x,curr_y])
            elif curr_y<=x:
                res.append([curr_x,curr_y])
                res.append([x,y])
            else:
                new=[min(x,curr_x),max(y,curr_y)]
                res.append(new)
        print(res)
        return len(intervals)-len(res)