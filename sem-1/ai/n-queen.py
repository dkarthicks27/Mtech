## Let's solve the n-queen problem. We want to find out all the distinct positions of placing n-queens in a n x n board, such that they
# don't attack each other


def DFS(n: int):
    columns = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."]*n for _ in range(n)]

    def backtrack(row):
        if row == n:
            res.append(["".join(board[i]) for i in range(n)])
            return
        
        for col in range(n):
            if col in columns or (row - col) in negDiag or (row + col) in posDiag:
                continue
            columns.add(col)
            posDiag.add(row+col)
            negDiag.add(row-col)

            board[row][col] = "Q"
            backtrack(row + 1)

            # Backtrack and undo the move
            board[row][col] = "."
            columns.remove(col)
            posDiag.remove(row + col)
            negDiag.remove(row - col)
    
    backtrack(0)
    return res

n = 4

print(DFS(n))