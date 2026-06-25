class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix[0]),len(matrix)
        l,r=0,r*c-1        
        while l<=r:
            mid=(l+r)//2
            new_r,new_c=mid//c,mid%c
            
            if matrix[new_r][new_c]==target:
                return True
            elif matrix[new_r][new_c]>target:
                r=mid-1
            else:
                l=mid+1

                
        return False
