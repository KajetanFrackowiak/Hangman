import random


def name_attempts(attempt):
    if attempt == 1:
        return "attempt"
    else:
        return "attempts"


def write_guessed_letters(word):
    guessed_letters_ = ""
    for element in word:
        guessed_letters_ += element
    return guessed_letters_


attempts = 8
wins = 0
losses = 0
print(f"H A N G M A N  # {attempts} {name_attempts(attempts)}")
while True:
    words_list = ["python", "java", "swift", "javascript"]
    answer = random.choice(words_list)
    answer = list(answer)
    attempts = 8
    hidden_answer = list("-" * len(answer))
    choose = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ').strip()
    if choose == "exit":
        break
    elif choose == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {losses} times.")
    else:
        while attempts > 0 and "-" in hidden_answer:
            guessed_letters = write_guessed_letters(hidden_answer)
            while True:
                print(f"\n{guessed_letters}")
                letter = input("Input a letter: ")
                if not len(letter) == 1:
                    print("Please, input a single letter.\n")
                elif not letter.islower() or not letter.isalpha():
                    print("Please, enter a lowercase letter from the English alphabet.\n")
                elif letter in hidden_answer:
                    print("You've already guessed this letter.")
                else:
                    break

            if letter in answer:
                if letter in hidden_answer:
                    attempts -= 1
                    print(f"No improvements.  # {attempts} {name_attempts(attempts)}")
                for i in range(len(hidden_answer)):
                    if answer[i] == letter:
                        hidden_answer[i] = letter
            else:
                attempts -= 1
                print(f"That letter doesn't appear in the word.  # {attempts} {name_attempts(attempts)}")

        if "-" not in hidden_answer and attempts > 0:
            print(f"You guessed the word {write_guessed_letters(hidden_answer)}!")
            print("You survived!")
            wins += 1
        else:
            print("\nYou lost!")
            losses += 1
