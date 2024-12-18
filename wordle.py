import random

# Display the game instructions and guide
def help_message():
    print("Welcome to the Word Guessing Game!")
    print("A player has to guess a hidden 5-letter word.")
    print("You have six attempts to find the hidden word.")
    print("Your Progress Guide:")
    print("- '✓' means the letter at that position is correct.")
    print("- '≈' means the letter is in the hidden word but in a different position.")
    print("- '✗' means the letter is not in the hidden word.")
    print("Good luck!\n")

# Read all valid words from the file
def get_words_from_file(file_path):
    """
    Reads a file containing valid words, filters only 5-letter words,
    and returns a list of words in lowercase.
    """
    try:
        words = []
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip().lower()
                if len(word) == 5:  # Only include 5-letter words
                    words.append(word)
        return words
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Make sure it exists in the directory.")
        exit()

# Randomly select a target word from the list of valid words
def get_target_word(allowed_words):
    """
    Returns a randomly selected word from the allowed words list.
    """
    return random.choice(allowed_words)

# Validate if the user's guess is valid
def is_guess_valid(guess, allowed_words):
    """
    Checks if the guess is:
    - Alphabetic
    - Exactly 5 letters long
    - Present in the list of allowed words
    """
    return guess.isalpha() and len(guess) == 5 and guess in allowed_words

# Score the user's guess and provide feedback
def evaluate_guess(guess, target_word):
    """
    Compares the guessed word with the target word and provides feedback:
    - '✓' for correct letter in the correct position
    - '≈' for correct letter in the wrong position
    - '✗' for incorrect letter
    """
    feedback = []  # List to store feedback for each letter
    target_char_count = {char: target_word.count(char) for char in target_word}

    # First pass: Check for exact matches (✓)
    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            feedback.append('✓')
            target_char_count[guess[i]] -= 1
        else:
            feedback.append(None)

    # Second pass: Check for misplaced letters (≈) and wrong letters (✗)
    for i in range(len(guess)):
        if feedback[i] is None:
            if guess[i] in target_char_count and target_char_count[guess[i]] > 0:
                feedback[i] = '≈'  # Correct letter, wrong position
                target_char_count[guess[i]] -= 1
            else:
                feedback[i] = '✗'  # Incorrect letter

    return ''.join(feedback)

# Main game logic
def game():
    """
    Implements the game logic:
    - Displays instructions
    - Prompts the player to guess the word
    - Validates guesses and provides feedback
    - Allows the player to play multiple rounds
    """
    help_message()
    allowed_file = "all_words.txt"  # File containing all valid words
    allowed_words = get_words_from_file(allowed_file)

    print("First five words:", allowed_words[:5])
    print("Last five words:", allowed_words[-5:])

    while True:  # Loop for replaying the game
        target_word = get_target_word(allowed_words)
        max_attempts = 6
        attempts = 0

        while attempts < max_attempts:
            guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your 5-letter guess: ").strip().lower()

            if not is_guess_valid(guess, allowed_words):
                print(f"Invalid guess! Make sure '{guess}' is a valid 5-letter word from the word list.\n")
                continue

            feedback = evaluate_guess(guess, target_word)
            print(f"Feedback: {feedback}")

            if guess == target_word:
                print("Congratulations! You've guessed the word correctly!")
                break

            attempts += 1

            if attempts == max_attempts:
                print("Sorry, you've run out of attempts. Better luck next time!")
                print(f"The hidden word was: {target_word}")
            else:
                print(f"You have {max_attempts - attempts} attempt(s) left.\n")
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
 
if __name__ == "__main__":
    print("\nStarting the game...\n")
    # Start the game
    game()
