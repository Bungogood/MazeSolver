class nqueens:
    def __init__(self, board, s):
        self.s = s
        self.board = [[board[row][col] for col in range(s)] for row in range(s)]
    
    def __str__(self):
        return "\n".join([",".join(["Q" if self.board[row][col] else " " for col in range(self.s)]) for row in range(self.s)]) + "\n"

def valid(board, row, col, s): 
    for i in range(col): 
        if board[row][i]: 
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j]: 
            return False
    
    for i, j in zip(range(row, s, 1), range(col, -1, -1)): 
        if board[i][j]: 
            return False
    
    return True

def solveprocess(board, col, sln, s):
    if col == s:
        sln.append(nqueens(board, s))
        return
    for i in range(s): 
        if valid(board, i, col, s): 
            board[i][col] = True
            solveprocess(board, col + 1, sln, s)
            board[i][col] = False

def solve(s):
    board = [[False for col in range(s)] for row in range(s)]
    sln = []
    solveprocess(board, 0, sln, s)
    return sln

solve(8)