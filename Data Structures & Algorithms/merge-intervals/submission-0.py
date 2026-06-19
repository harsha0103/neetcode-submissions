class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res=[intervals[0]]

        for i in intervals[1:]:
            curr_x,curr_y=res.pop()

            if curr_y<i[0]:
                res.append([curr_x,curr_y])
                res.append(i)
            elif curr_x>i[1]:
                res.append(i)
                res.append([curr_x,curr_y])
            else:
                new_intr=[min(i[0],curr_x),max(i[1],curr_y)]
                res.append(new_intr)
        return res
            