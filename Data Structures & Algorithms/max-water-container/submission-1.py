class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        res=0
        while l<r:
            hei=min(heights[l],heights[r])
            res=max(hei*(r-l),res)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
                       
        return res