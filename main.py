import random

print("Welcome to Rock-Paper-Scissors with Scoreboard!")

choices = ["rock", "paper", "scissors"]

# Scoreboard
user_score = 0
ai_score = 0
ties = 0

while True:
    user_choice = input("\nEnter rock/paper/scissors or 'q' to quit: ").lower()

    if user_choice == 'q':
        print("\nFinal Scoreboard:")
        print(f"Your Score: {user_score}")
        print(f"Computer Score: {ai_score}")
        print(f"Ties: {ties}")
        print("Thanks for playing! 😊")
        break

    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    ai_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {ai_choice}")

    if user_choice == ai_choice:
        print("It's a tie!")
        ties += 1

    elif (
        (user_choice == "rock" and ai_choice == "scissors") or
        (user_choice == "paper" and ai_choice == "rock") or
        (user_choice == "scissors" and ai_choice == "paper")
    ):
        print("🎉 You win!")
        user_score += 1
    else:
        print("💻 Computer wins!")
        ai_score += 1

    print("\nCurrent Score:")
    print(f"You: {user_score} | Computer: {ai_score} | Ties: {ties}")
