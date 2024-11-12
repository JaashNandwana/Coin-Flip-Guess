import random

def coin_flip():
    # Welcome message
    print("Welcome to the Coin Flip Game!")
    
    # Player's guess
    player_guess = input("Guess heads or tails: ").strip().lower()
    if player_guess not in ["heads", "tails"]:
        print("Invalid choice. Please choose 'heads' or 'tails'.")
        return

    # Coin flip result
    flip_result = random.choice(["heads", "tails"])
    print(f"The coin landed on {flip_result}.")

    # Check if the player won
    if player_guess == flip_result:
        print("Congratulations! You guessed correctly.")
    else:
        print("Sorry, better luck next time!")

# Run the game
coin_flip()

