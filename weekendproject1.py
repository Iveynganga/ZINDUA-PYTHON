import random

options = ("Rock", "Paper", "Scissors")
random= ("Rock", "Paper", "Scissors")

user_score, computer_score = 0,0
totalrounds = 3

for i in range(totalrounds):
    userOption = int(input('Press 1 for Rock, 2 for Paper, 3 for Scissors: '))
    userChoice = options[userOption-1]

    computerChoice = options[random(0,2)]


print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)

if user_choice == computer_choice:
        print("It's a tie!")
        result =0    

elif user_choice =="Rock" and computer_choice =="Scissors" :
    print("You've won")
user_score += 1

if user_choice == "Paper" and computer_choice == "Rock":
    print("You've won")
    user_score += 1

elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You've won")
    user_score += 1

else:
    print("Computer wins")

print(f'Your score: {user_score}')
print(f"Computer's score: {computer_score}")

if user_score > computer_score:
    print('You won most rounds!')

elif computerscore > userscore:
    print('Computer won most rounds!')
else: 
    print("It's a draw")