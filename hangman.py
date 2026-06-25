import random

words = ["python", "apple", "computer", "school", "mobile"]

word = random.choice(words)
display = ["_"] * len(word)

used = []
chance = 6

print("Welcome to Hangman")

while chance > 0:

    print("\nWord:", " ".join(display))
    print("Chances left:", chance)

    letter = input("Enter a letter: ").lower()

    if len(letter) != 1:
        print("Please enter only one letter.")
        continue

    if letter in used:
        print("You already entered this letter.")
        continue

    used.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
        print("Correct!")
    else:
        chance -= 1
        print("Wrong!")

    if "_" not in display:
        break

if "_" not in display:
    print("\nYou won!")
    print("The word was:", word)
else:
    print("\nYou lost!")
    print("The word was:", word)
