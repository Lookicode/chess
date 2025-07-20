import chess
import random

def get_engine_move(board: chess.Board) -> chess.Move:
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

        engine_move = get_engine_move(board)
        board.push(engine_move)
        print("\nEngine played:", engine_move.uci())
        print(board)

    print("\nGame over!")
    print("Result:", board.result())

if __name__ == "__main__":
    main()
