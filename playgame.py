import random

def play_game():
    words = ["apple", "banana", "cherry", "dog", "elephant"]
    secret_word = random.choice(words)
    attempts = 3
    guessed_word = ["_"] * len(secret_word)

    print("Welcome to the Guess the Word game!")

    while attempts > 0 and "_" in guessed_word:
        print(" ".join(guessed_word))
        guess = input(f"Guess a letter or the whole word ({attempts} attempts left): ").lower()

        if len(guess) == 1:
            if guess in secret_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        guessed_word[i] = guess
            else:
                attempts -= 1
        elif guess == secret_word:
            guessed_word = list(secret_word)

    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Out of attempts! The word was: {secret_word}")

if __name__ == "__main__":
    play_game()
