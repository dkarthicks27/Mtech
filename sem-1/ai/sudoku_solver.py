board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
def checkRow(row_no):
    return [int(board[row_no][j]) for j in range(0, 9) if board[row_no][j] != '.']

def checkCol(col_no):
    return [int(board[i][col_no]) for i in range(0, 9) if board[i][col_no] != '.']

def checkMat(r, c):
    nums = []
    for i in range(r, r+3):
        for j in range(c, c+3):
            if board[i][j] != '.':
                nums.append(int(board[i][j]))
    
    return nums

def checkValidity(curr_i, curr_j, num):
    bound_x = (curr_i // 3) * 3
    bound_y = (curr_j // 3) * 3

    if num not in checkRow(curr_i) and num not in checkCol(curr_j) and num not in checkMat(bound_x, bound_y):
        return True
    return False

    
def backtrack(row, col):
    print(f"Current row, col: {row}, {col}")
    if row == 9:
        return True
    
    next_row = row + (col + 1) // 9
    next_col = (col + 1) % 9

    if board[row][col] != '.':
        return backtrack(next_row, next_col)

    for num in range(1, 10):
        if checkValidity(row, col, num):
            board[row][col] = str(num)
            if backtrack(next_row, next_col):
                return True
            board[row][col] = '.'
    
    return False


backtrack(0, 0)

print(board)