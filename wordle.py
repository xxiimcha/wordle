import random  # Make sure to import the random module

def help_message():
    print("Welcome to the Word Guessing Game!")
    print("You have to guess the target word within a limited number of tries.")
    print("The word must be valid (e.g., a single word). Good luck!")

def get_target_word(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
            return random.choice(words)  # Use random to select a word
    except FileNotFoundError:
        print("Target words file not found. Make sure 'target_words.txt' is available.")
        exit()

def is_guess_valid(guess):
    # Check if the guess is valid (e.g., a single word, alphabetic)
    return guess.isalpha()

def score_guess(guess, target_word):
    # A basic scoring system: return True if the guess matches the target word
    return guess.lower() == target_word.lower()

def game():
    help_message()
    target_file = "target_words.txt"  # File containing target words
    target_word = get_target_word(target_file)
    max_tries = 5
    tries = 0
    
    while tries < max_tries:
        guess = input(f"Attempt {tries + 1}/{max_tries}: Enter your guess: ").strip()
        
        if not is_guess_valid(guess):
            print("Invalid guess! Please enter a valid word.")
            continue
        
        if score_guess(guess, target_word):
            print("Congratulations! You've guessed the word correctly!")
            return
        
        tries += 1
        
        if tries == max_tries:
            print("Sorry, you've run out of tries. Better luck next time!")
            print(f"The target word was: {target_word}")
            return
        else:
            print("Incorrect guess! Try again.")
    
if __name__ == "__main__":
    game()
