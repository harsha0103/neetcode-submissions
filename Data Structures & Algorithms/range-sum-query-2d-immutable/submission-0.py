class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row=len(matrix)
        col=len(matrix[0])
        self.prefix=[[0]* (col+1) for i in range(row+1)]
        for i in range(row):
            prefix=0
            for j in range(col+1):
                self.prefix[i+1][j]=prefix
                if j<col:
                    prefix+=matrix[i][j]
        print(self.prefix)

        for i in range(col+1):
            prefix=0
            for j in range(row+1):
                prefix+=self.prefix[j][i]
                self.prefix[j][i]=prefix
        print(self.prefix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return 0


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)