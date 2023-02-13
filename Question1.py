# Store the player's names and the highest score
player1_name = ""
player2_name = ""
highest_score = 0

# Function to get the player's move
def get_move(player_name):
    move = input(f"{player_name}, enter your move (rock, paper, scissors): ")
    while move not in ["rock", "paper", "scissors"]:
        move = input("Invalid move. Please enter 'rock', 'paper', or 'scissors': ")
    return move

# Function to determine the winner
def determine_winner(player1_move, player2_move):
    if player1_move == player2_move:
        return "draw"
    elif player1_move == "rock" and player2_move == "scissors":
        return "player1"
    elif player1_move == "scissors" and player2_move == "paper":
        return "player1"
    elif player1_move == "paper" and player2_move == "rock":
        return "player1"
    else:
        return "player2"

# Main game loop
while True:
    print("Welcome to Rock, Paper, Scissors!")
    if player1_name == "":
        player1_name = input("Enter Player 1 name: ")
    if player2_name == "":
        player2_name = input("Enter Player 2 name: ")
    
    player1_move = get_move(player1_name)
    player2_move = get_move(player2_name)

    winner = determine_winner(player1_move, player2_move)
    if winner == "draw":
        print("It's a draw!")
    elif winner == "player1":
        print(f"{player1_name} wins with {player1_move} against {player2_move}!")
        # Update highest score if player1 wins
        highest_score = max(highest_score, 1)
    else:
        print(f"{player2_name} wins with {player2_move} against {player1_move}!")
        # Update highest score if player2 wins
        highest_score = max(highest_score, 1)

    print(f"The highest score is {highest_score}.")
    play_again = input("Do you want to play again (yes/no)? ")
    if play_again.lower() == "no":
        break

# Store the player names and highest score to a file for future use
with open("game_data.txt", "w") as file:
    file.write(f"{player1_name}\n{player2_name}\n{highest_score}\n")

print("Thank you for playing Rock, Paper, Scissors! Goodbye.")