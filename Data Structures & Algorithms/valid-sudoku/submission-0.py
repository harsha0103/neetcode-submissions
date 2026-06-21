class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            s1= set()
            s2= set()
            for j in range(9):
                if board[i][j]=='.' or board[j][i]=='.':
                    continue
                if board[i][j] in s1 or board[j][i] in s2:
                    return False
                s1.add(board[i][j])
                s2.add(board[j][i])
        
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                s1= set()

                for i in range(3):
                    for j in range(3):
                        if board[box_row+i][box_row+j] =='.':
                            continue
                        elif board[box_row+i][box_row+j] in s1:
                            return False
                        else:
                            s1.add(board[box_row+i][box_row+j])

        


        return True
            



        