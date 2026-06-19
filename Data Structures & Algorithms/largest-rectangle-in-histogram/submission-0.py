class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_rect=0
        for i,v in enumerate(heights):
            pi=i
            while stack and stack[-1][1]>v:
                index,pv=stack.pop()
                max_rect=max(max_rect,(i-index)*pv)
                pi=index
            stack.append((pi,v))
        
        while stack:
            pi,pv=stack.pop()
            max_rect=max(max_rect,(len(heights)-pi)*pv)
        return max_rect