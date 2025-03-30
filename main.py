# Number  Guessing game
import random

class NumberGuessingGame:
    
    def generate_random_number(self):
        return random.randint(1,100)
        

    def get_user_guess(self):
        while True:
            try:
                user_input = input("Enter your guess (between 1 and 100): ")
                guess = int(user_input)
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play_game(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("It's your turn to guess the number!")

        # Generate the secret number
        secret = self.generate_random_number()
        attempts = 0

        while True:
            user_input = self.get_user_guess()
            attempts += 1
            
            if user_input > secret:
                print("Too high! Try again.")
            elif user_input < secret:
                print("Too low! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret} in {attempts} attempts.")
                break

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play_game()
    
