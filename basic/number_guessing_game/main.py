# Number  Guessing game
import random

class NumberGuessingGame:
    
    def __init__(self):
        self.difficulty = None
        self.lower_bound = 1
        self.upper_bound = 100
        self.max_attempts = None
        self.secret_number = None
        self.attempts = 0
    
    def generate_random_number(self):
        secret_number = random.randint(self.lower_bound, self.upper_bound)
        return secret_number
        

    def get_user_guess(self):
        while True:
            try:
                user_input = input("Enter your guess (between 1 and 100): ")
                guess = int(user_input)
                if self.lower_bound <= guess <= self.upper_bound:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def user_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice (1/2/3): "))
                if 1 <= choice <= 3:
                    print("Let's begin the game!")
                    return choice
                else:
                    print("Invalid input. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def set_difficulty(self):   
        difficulty_settings = {
            1: {
                "range": (1, 50),
                "attempts": float('inf')
                },  # Easy
            2: {
                "range": (1, 100),
                "attempts": 10
                },          # Medium
            3: {
                "range": (1, 100),
                "attempts": 5
                },           # Hard
        }
        settings = difficulty_settings[self.difficulty]
        self.lower_bound, self.upper_bound = settings["range"]
        self.max_attempts = settings["attempts"]
                
    def play_game(self):
        print("======================================")
        print("Welcome to the Number Guessing Game!")
        print("======================================")
        print("Choose a difficulty level:")
        print("1. Easy (1–50, unlimited attempts)")
        print("2. Medium (1–100, limited to 10 attempts)")
        print("3. Hard (1–100, limited to 5 attempts)")
        print("======================================")
        self.difficulty = self.user_choice()
        print("======================================")
        print("I'm thinking of a number between 1 and 100.")
        print("It's your turn to guess the number!")
        print("======================================")

        # Generate the secret number
        self.secret_number = self.generate_random_number()
        self.attempts = 0
        self.set_difficulty()
            
        while self.attempts < self.max_attempts:
            user_input = self.get_user_guess()
            self.attempts += 1
            
            if user_input > self.secret_number:
                print(f"Too high! Try again. Attempts left: {self.max_attempts - self.attempts}")
            elif user_input < self.secret_number:
                print(f"Too low! Try again. Attempts left: {self.max_attempts - self.attempts}")
            else:
                print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts. Left out attempts {self.max_attempts - self.attempts}")
                break
        else:
            print(f"Better Luck Next TIME! You have wasted all your {self.attempts} attempts.")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play_game()
    
