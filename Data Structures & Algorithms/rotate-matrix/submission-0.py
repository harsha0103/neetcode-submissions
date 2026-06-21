class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        res=[[]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[i][j]=matrix[j][i]
        
        print(res)

