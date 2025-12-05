import random

# 5 predefined words
words = ["apple", "tiger", "computer", "river", "flower"]

# randomly choose one word
secret_word = random.choice(words)

# create a list with underscores, same size as secret_word
guessed = ["_"] * len(secret_word)

# to track incorrect guesses
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while wrong_guesses < max_wrong and "_" in guessed:
    print("Word:", " ".join(guessed))
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")

    letter = input("Enter a letter: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    if letter in guessed or letter in secret_word and letter in guessed:
        print("You already guessed that letter.\n")
        continue

    # check if letter is in the secret word
    if letter in secret_word:
        print("✔ Correct guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                guessed[i] = letter
    else:
        wrong_guesses += 1
        print("❌ Wrong guess.\n")

# end of loop
print("\n-------------------------------")
if "_" not in guessed:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("😢 Game Over! The word was:", secret_word)
print("-------------------------------")
