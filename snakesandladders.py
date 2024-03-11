import random

def get_position(player, position):
    if position in snakes:
        print(f"Oops! Player {player} got bitten by a snake. Going down to {snakes[position]}!")
        position = snakes[position]
    elif position in ladders:
        print(f"Wow! Player {player} found a ladder. Climbing up to {ladders[position]}!")
        position = ladders[position]
    return position

def dice_roll(player, position):
    dice_result = random.randint(1, 6)
    print(f"Player {player} rolled a {dice_result}")
    position == dice_result
    position = get_position(player, position)
    return position

def snake_and_ladder(player1, player2, position1, position2):
    position1 = dice_roll(player1, position1)
    if position1 >= 100:
        return f"Player {player1} wins!"

    position2 = dice_roll(player2, position2)
    if position2 >= 100:
        return f"Player {player2} wins!"

    return position1, position2



