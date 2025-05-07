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

# TODO: Keep score between rounds
# TODO: Allow multiple rounds with option to quit
# TODO: Add colored output (green = win, red = lose, yellow = draw)
# TODO: Add test cases
# TODO: Add a GUI version using Tkinter

def main():
    print("Welcome to Rock Paper Scissors Game!")
    user_choice = get_user_choice()
    if user_choice is None:
        return
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = decide_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
