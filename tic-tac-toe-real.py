# This is the game for the tic-tac-toe based on the python
# Global declaration

tac_toe = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def display_tac_toe():
    print("")
    print("     0  1  2")
    for row in enumerate(tac_toe):
        print(row)

# Function to process the number placement and winner
def check_winner(board):

    # Check rows for a winner
    for row in board:
        print(row)
        if row[0] == row[1] == row[2] and row[0] != 0:
            return f"Winner found: {row[0]}"

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return f"Winner found: {board[0][col]}"

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return f"Winner found: {board[0][0]}"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return f"Winner found: {board[0][2]}"

    return None  # No winner yet


# starter questions
print("")
print("Welcome to tic-tac-toe game by Nadzirah")
print("This game need 2 player on a 3x3 grid. The players take turns marking the spaces in the grid with their respective symbols—traditionally. The objective is to be the first player to place three of their symbols in a row, either horizontally, vertically, or diagonally.")
print("")

print("Do you want to play? (y/n)")
decision = input()

if decision == 'y':

    print("Please enter first player number:")
    first_player = input()
    
    if first_player == '0':
        print("Don't enter number '0'")
    else: 
        print("Please enter second player number:")
        second_player = input()

        if second_player == '0':
            print("Don't enter number '0'")
        else:
            
            if second_player == first_player:
                print("Second player, your number cannot be same as first player")

            else:
                print("This is the grid and number for row and column")
                # display the list of grid 
                display_tac_toe()

                count = 0
                # alternate between 2 users
                players = [first_player, second_player]
                current_turn = 0

                while count <= 6:
                    print("")
                    print(f"Player {players[current_turn]} it's your turn.")
                    
                    print("Enter which row you want")
                    row_input = input()
                    row_number = int(row_input)

                    print("Enter which column you want")
                    column_input = input()
                    column_number = int(column_input)

                    print("")

                    tac_toe[row_number][column_number] = players[current_turn]

                    winner = check_winner(tac_toe)

                    print(winner)
                    if winner:
                        print(f"Player {players[current_turn]} is the winner!!!!.")
                        break
                    
                    current_turn = 1 - current_turn
                    count += 1
                        

else:
    print("Bye-Bye!")











    
