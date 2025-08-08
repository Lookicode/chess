import chess

from evaluate_board import evaluate_board
from config import MIN, MAX


def alphabeta(board: chess.Board, depth: int, alpha: int, beta: int, maximizing: bool) -> int:
    """Alpha-Beta pruning algorithm for minimax.
    
    Works by recursively evaluating the board state and pruning branches
    that won't affect the final decision, thus optimizing the search process.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing:
        value = MIN
        for move in board.legal_moves:
            board.push(move)
            value = max(value, alphabeta(board, depth - 1, alpha, beta, False))
            board.pop()
            alpha = max(alpha, value)
            if alpha >= beta:  # beta cut-off
                break
        return value
    else:
        value = MAX
        for move in board.legal_moves:
            board.push(move)
            value = min(value, alphabeta(board, depth - 1, alpha, beta, True))
            board.pop()
            beta = min(beta, value)
            if alpha >= beta:  # alpha cut-off
                break
        return value