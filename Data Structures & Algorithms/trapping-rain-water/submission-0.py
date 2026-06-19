class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1

        max_left,max_right=height[left],height[right]
        total_water=0

        while right>=left:

            if max_left<=max_right:
                current= max_left-height[left]
                if current>0:
                    total_water+=current
                max_left=max(max_left,height[left])
                left+=1
            
            elif max_right<max_left:
                current= max_right-height[right]
                if current>0:
                    total_water+=current
                max_right=max(max_right,height[right])
                right-=1
        return total_water