import chess
import random

from minimax import minimax
import config

def get_engine_move(board: chess.Board, depth: int = 2) -> chess.Move:
    """Returns the best move using minimax."""
    best_move = None
    best_value = float("-inf") if board.turn == chess.WHITE else float("inf")

    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, not board.turn)
        board.pop()

        if board.turn == chess.WHITE and board_value > best_value:
            best_value = board_value
            best_move = move
        elif board.turn == chess.BLACK and board_value < best_value:
            best_value = board_value
            best_move = move
            
    assert best_move is not None, "No legal moves found, but game is not over"
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
        engine_move = get_engine_move(board, depth=config.DEPTH)
        board.push(engine_move)
        print("\nEngine played:", engine_move.uci())
        print(board)

    print("\nGame over!")
    print("Result:", board.result())

if __name__ == "__main__":
    main()
