import random

options = ("Rock", "Paper", "Scissors")

user_score, computer_score = 0, 0
total_rounds = 3

for i in range(total_rounds):
    user_option = int(input('Press 1 for Rock, 2 for Paper, 3 for Scissors: '))
    user_choice = options[user_option - 1]

    computer_choice = random.choice(options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You've won!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

print(f'Your score: {user_score}')
print(f"Computer's score: {computer_score}")

if user_score > computer_score:
    print('You won most rounds!')
elif computer_score > user_score:
    print('Computer won most rounds!')
else:
    print("It's a draw")