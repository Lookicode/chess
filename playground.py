import chess

board = chess.Board()
print(board)

for move in board.legal_moves:
    print(move)

print(board.push_san("e4"))