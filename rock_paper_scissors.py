import random

def get_user_choice():
    print("Choose one: rock, paper, or scissors")
    choice = input("Your choice: ").lower()
    if choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice!")
        return None
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("🎮 Welcome to Rock Paper Scissors Game!")
    
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            continue
        
        computer_choice = get_computer_choice()
        print(f"💻 Computer chose: {computer_choice}")
        result = decide_winner(user_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        while True:
            again = input("Play again? (Y/N): ").strip().lower()
            if again in ['y', 'yes']:
                break  # Start a new round
            elif again in ['n', 'q', 'no']:
                print("👋 Thanks for playing!")
                return
            else:
                print("❗ Invalid input. Please enter 'Y' to play again or 'N' to quit.")

if __name__ == "__main__":
    main()
