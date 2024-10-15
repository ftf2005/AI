player, opponent = 'x', 'o'

def isMovesLeft(board):
    return any(cell == '_' for row in board for cell in row)

def evaluate(b):
    for row in b:
        if row.count(player) == 3: return 10
        if row.count(opponent) == 3: return -10
    for col in range(3):
        if all(b[row][col] == player for row in range(3)): return 10
        if all(b[row][col] == opponent for row in range(3)): return -10
    if b[0][0] == b[1][1] == b[2][2]: return 10 if b[0][0] == player else -10
    if b[0][2] == b[1][1] == b[2][0]: return 10 if b[0][2] == player else -10
    return 0

def minimax(board, isMax):
    score = evaluate(board)
    if score != 0 or not isMovesLeft(board): return score
    best = -1000 if isMax else 1000
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player if isMax else opponent
                best = max(best, minimax(board, not isMax)) if isMax else min(best, minimax(board, not isMax))
                board[i][j] = '_'
    return best

def findBestMove(board):
    bestVal, bestMove = -1000, (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove, bestVal = (i, j), moveVal
    return bestMove

# Driver code
board = [['x', 'o', 'x'], ['o', 'o', 'x'], ['_', '_', '_']]
bestMove = findBestMove(board)
print("Optimal Move: ROW:", bestMove[0], "COL:", bestMove[1])
