class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=len(board)
        col=len(board[0])
        for i in range(9):
            for j in range(9):
                row_set=set()
                if board[i][j]!='.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
        
        for i in range(9):
            for j in range(9):
                col_set=set()
                if board[j][i]!='.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                box=set()
                for k in range(3):
                    for m in range(3):
                        temp=board[k+i][m+j] 
                        if temp in box and temp!='.':
                            return False
                        box.add(board[k+i][m+j])
        return True
                
