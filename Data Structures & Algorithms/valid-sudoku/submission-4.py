class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows and columns
        for i in range(9):
            s1 = set()  # For row
            s2 = set()  # For column
            for j in range(9):
                # Skip empty cells
                if board[i][j] == '.' and board[j][i] == '.':
                    continue
                
                # Check duplicates in row and column
                if board[i][j] != '.' and board[i][j] in s1:
                    return False
                if board[j][i] != '.' and board[j][i] in s2:
                    return False
                
                s1.add(board[i][j])
                s2.add(board[j][i])
                
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                s1= set()

                for i in range(3):
                    for j in range(3):
                        val = board[box_row+i][box_col+j]
                        if  val =='.':
                            continue
                        if val in s1:
                            return False
                        s1.add(val)

        return True
            



        