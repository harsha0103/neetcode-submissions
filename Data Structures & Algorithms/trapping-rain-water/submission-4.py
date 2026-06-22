class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_left,max_right=height[l],height[r]
        total=0
        while l<=r:
            if max_left>=max_right:
                temp=max_right-height[r]
                total+=temp if temp>0 else 0
                max_right=max(max_right,height[r])
                r-=1
            else:
                temp=max_left-height[l]
                total+=temp if temp>0 else 0
                max_left=max(max_left,height[l])
                l+=1
        
        return total