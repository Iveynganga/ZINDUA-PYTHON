
options = ("Rock", "Paper", "Scissors")
random= ("Rock", "Paper", "Scissors")

user_choice = input("Choose Rock, Paper, or Scissors: ")
computer_choice = input("Choose Random: ")

print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)

if user_choice == computer_choice :

    print("it's a tie")

elif user_choice =="Rock" and computer_choice =="Scissors" :
    print("You've won")

elif user_choice =="Paper" and computer_choice =="Rock" :
    print("You've won")

elif user_choice =="Scissors" and computer_choice =="Paper" :
    print("You've won")

else :
    print("Computer wins")
