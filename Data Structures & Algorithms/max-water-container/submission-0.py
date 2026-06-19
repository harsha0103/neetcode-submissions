class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start,end=0,len(heights)-1
        container=0
        while start<end:
            minimum=min(heights[start],heights[end])
            container= max(container, minimum*(end-start))
            if heights[start]<heights[end]:
                start+=1
            elif heights[start]>heights[end]:
                end-=1
            else:
                start+=1
                end-=1

        return container

        