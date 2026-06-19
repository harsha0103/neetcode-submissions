class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        res=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[i][j]=matrix[j][i]
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=res[i][j]


