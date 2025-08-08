from typing import Optional
import chess
import random

from alphabeta import alphabeta
from config import MIN, MAX, DEPTH

def get_engine_move(board: chess.Board, depth: int = 3) -> chess.Move:
    """Get the best move for the engine using minimax with alpha-beta pruning."""
    def move_score(m: chess.Move) -> int:
        return 1 if board.is_capture(m) else 0

    # Simplest heuristic: prioritize captures
    ordered_moves = sorted(board.legal_moves, key=move_score, reverse=True)

    best_move: Optional[chess.Move] = None
    if board.turn == chess.WHITE:
        best_val = MIN
        for move in ordered_moves:
            board.push(move)
            val = alphabeta(board, depth - 1, MIN, MAX, False)
            board.pop()
            if val > best_val:
                best_val = val
                best_move = move
    else:
        best_val = MAX
        for move in ordered_moves:
            board.push(move)
            val = alphabeta(board, depth - 1, MIN, MAX, True)
            board.pop()
            if val < best_val:
                best_val = val
                best_move = move

    assert best_move is not None, "No legal moves found; position should be game-over."
    return best_move



def get_random_move(board: chess.Board) -> chess.Move:
    """Stub engine move: pick a random legal move."""
    return random.choice(list(board.legal_moves))

def main():
    board = chess.Board()
    print("Welcome to your chess engine CLI!")
    print(board)

    while not board.is_game_over():
        print("\nYour turn. Enter your move in UCI format (e.g., e2e4):")
        user_input = input(">>> ").strip()

        if user_input == "exit":
            print("Exiting game.")
            break

        try:
            move = chess.Move.from_uci(user_input)
            if move in board.legal_moves:
                board.push(move)
                print("\nBoard after your move:")
                print(board)
            else:
                print("Illegal move. Try again.")
                continue
        except ValueError:
            print("Invalid input format. Try again.")
            continue

        if board.is_game_over():
            break

        # Get the engine's move using minimax
        engine_move = get_engine_move(board, depth=DEPTH)
        board.push(engine_move)
        print("\nEngine played:", engine_move.uci())
        print(board)

    print("\nGame over!")
    print("Result:", board.result())

if __name__ == "__main__":
    main()
