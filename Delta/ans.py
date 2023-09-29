import random
def choose_random_word():
    word_list = ["a", "b", "c", "d","e","f","g"]
    return random.choice(word_list)
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display
def hangman():
    word_to_guess=choose_random_word().lower()
    guessed_letters = []
    strikes = 0
    print("Welcome to Hangman!")
    print("Try to guess the word. You can make 5 wrong guesses.")
    while True:
        print("\nWord:",display_word(word_to_guess, guessed_letters))
        print("Guessed letters:",",".join(guessed_letters))
        guess = input("Guess a letter (or type 'quit' to exit): ").lower()
        if guess == "quit":
            print(f"The word was '{word_to_guess}'. Goodbye!")
            break
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess!")
            strikes += 1
        if strikes >= 5:
            print("You've reached 5 strikes. Game over!")
            print(f"The word was '{word_to_guess}'.")
            break
        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You've guessed the word:", word_to_guess)
            break
if __name__ == "__main__":
    hangman()