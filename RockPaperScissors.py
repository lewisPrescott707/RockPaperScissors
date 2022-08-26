import computer

win = 0
defeat = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    # rock: 0, paper: 1, scissors: 2
    guess = computer.pick(options)
    print("Computer picked", guess + ".")

    if user_input == "paper" and guess == "rock":
        print("You won!")
        win += 1
    elif user_input == "rock" and guess == "scissors":
        print("You won!")
        win += 1
    elif user_input == "scissors" and guess == "paper":
        print("You won!")
        win += 1
    elif user_input == "scissors" and guess == "scissors" or user_input == "paper" and guess == "paper" or user_input == "rock" and guess == "rock":
        print("It's a draw!")
        continue
    else:
        print("You lost!")
        defeat += 1
if win >= defeat:
    print("Congratulation! You won", win, "times.")
    print("The computer won", defeat, "times.")
else:
    print("Better luck next time! You won", win, "times.")
    print("The computer won", defeat, "times.")

print("Bye!")
