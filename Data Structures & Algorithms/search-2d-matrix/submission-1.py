class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,c=len(matrix),len(matrix[0])
        l,r=0,row*c-1

        while l<=r:
            mid=l+(r-l)//2
            row,col=mid//c,mid%c

            if matrix[row][col]>target:
                r=mid-1
            elif matrix[row][col]<target:
                l=mid+1
            else:
                return True
        return False