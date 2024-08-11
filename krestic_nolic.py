def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

            if not (0 <= row <= 2) or not (0 <= col <= 2):
                print("Invalid row or column. Please enter numbers between 0 and 2.")
                continue

            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                continue

            board[row][col] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        except ValueError:
            print("Invalid input. Please enter integers between 0 and 2.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()