import random

def dice():
    return random.randint(1, 6)

player_1 = input("Enter name of player-1: ")
player_2 = input("Enter name of player-2: ")
player1_score, player2_score = 0, 0
winning_point = 100

ladders = {3: 22, 5: 8, 11: 26, 20: 29}
snakes = {17: 4, 19: 7, 27: 1, 39: 3, 50: 34, 70: 55, 80: 60, 82: 57, 88: 24}
current_player = 1

while player1_score < winning_point and player2_score < winning_point:
    player_name = player_1 if current_player == 1 else player_2
    player_score = player1_score if current_player == 1 else player2_score
    status = input(f"({player_name}): [P]lay or [Q]uit: ").strip().lower()

    if status == 'q':
        print(f"{player_name} quit the game. Goodbye!")
        break
    if status != 'p':
        print("Invalid choice. Enter 'P' to play or 'Q' to quit.")
        continue

    dice_roll = dice()
    print(f"Dice Score: {dice_roll}")
    player_score += dice_roll

    if player_score > winning_point:
        player_score -= dice_roll
        print(f"Need exactly {winning_point} to win. Stay at {player_score}.")
    else:
        if player_score in ladders:
            player_score = ladders[player_score]
            print(f"++++++ Ladder! New position: {player_score}")
        elif player_score in snakes:
            player_score = snakes[player_score]
            print(f"----- Snake! New position: {player_score}")
        else:
            print(f"Current position: {player_score}")

    if current_player == 1:
        player1_score = player_score
    else:
        player2_score = player_score

    print(f"{player_1}: {player1_score} | {player_2}: {player2_score}\n")

    if player1_score == winning_point:
        print(f"********* {player_1} won the game! *********")
        break
    if player2_score == winning_point:
        print(f"********* {player_2} won the game! *********")
        break

    current_player = 2 if current_player == 1 else 1      