import os

print(os.getcwd())
import random
games = 0
wins = 0
losses = 0
best_score = 0
save_exists = False

def show_menu():
    print("==============================")
    print("   GUESS THE NUMBER v1.1.1")
    print("==============================")
    print("         Welcome!     ")
    print()
    print("Choose the difficulty:")
    print("1 - Easy (1-10, 10 attempts)")
    print("2 - Medium (1-50, 7 attempts)")
    print("3 - Hard (1-100, 5 attempts)")
    print("==============================")

def show_statistics():
    print("=====Statistics=====")
    print("Games played:", games)
    print("Wins:", wins)
    print("Losses:", losses)
    if best_score == 0:
        print("No record yet")
    else:
        print("Best score:", best_score, "attempts")
    print("=====================")

def show_loading():
    print("==========================")
    print("     Loading save...      ")
    print("==========================")
    print("      Save loaded!        ")
    print("Games:", games)
    print("Wins:", wins)
    print("Losses:", losses)
    if best_score == 0:
        print("Best: No record")
    else:
        print("Best:", best_score, "attempts")
    print("==========================")

def ask_guess():
    while True:
        try:
            guess = int(input("Guess the number: "))
            return guess
        except:
            print("Please enter a number!")

def choose_difficulty():
    while True:
        try:
            difficulty = int(input("Choose difficulty: "))
        except:
            print("Please enter 1, 2 or 3!")
            continue
        if difficulty == 1:
            return random.randint(1, 10), 10, "Easy", 10
        elif difficulty == 2:
            return random.randint(1, 50), 7, "Medium", 50
        elif difficulty == 3:
            return random.randint(1, 100), 5, "Hard", 100
        else:
            print("Please choose 1, 2 or 3!")

def check_guess(secret, guess):
    return guess == secret

def play_game():
    global games, wins, losses, best_score
    games += 1
    secret, max_attempts, difficulty_name, max_number = choose_difficulty()
    print("You chose", difficulty_name, "mode!")
    print("Guess a number between 1 and", max_number)
    attempts = 0
    while True:
        guess = ask_guess()
        attempts += 1
        if check_guess(secret, guess):
            wins += 1
            if best_score == 0 or attempts < best_score:
                best_score = attempts
                save_best_score(best_score)
                print("New record!")
            print("Correct! You guessed in", attempts, "attempts")
            save_statistics()
            show_statistics()
            break
        else:
            if attempts >= max_attempts:
                losses += 1
                print("Game Over!")
                print("The secret number was", secret)
                save_statistics()
                show_statistics()
                break
            if secret > guess:
                print("Wrong! Too high!")
            else:
                print("Wrong! Too low!")
            print("Attempts left:", max_attempts - attempts)

def load_best_score():
    try:
        file = open("record.txt", "r")
        text = file.read()
        file.close()
        return int(text)
    except:
        return 0

def save_best_score(score):
    print("Save")
    file = open("record.txt", "w")
    file.write(str(score))
    file.close()

def load_statistics():
    global games, wins, losses, best_score, save_exists
    try:
        file = open("stats.txt", "r")
        text = file.read()
        file.close()
        lines = text.splitlines()
        for line in lines:
            data = line.split("=")
            if data[0] == "Games":
                games = int(data[1])
            elif data[0] == "Wins":
                wins = int(data[1])
            elif data[0] == "Losses":
                losses = int(data[1])
            elif data[0] == "Best":
                best_score = int(data[1])
                save_exists = True
    except FileNotFoundError:
        print("No statistics found. Starting new game")

def save_statistics():
    file = open("stats.txt", "w")
    file.write("Games=" + str(games) + "\n")
    file.write("Wins=" + str(wins) + "\n")
    file.write("Losses=" + str(losses) + "\n")
    file.write("\nBest=" + str(best_score))
    file.close()

def start_game():
    while True:
        play_game()
        while True:
            print()
            answer = input("Play again? (y/n): ")
            if answer == "y":
                break
            elif answer == "n":
                save_statistics()
                show_statistics()
                print("Thanks for playing!")
                return
            else:
                print("Please type y or n!")

best_score = load_best_score()
load_statistics()
if save_exists:
    show_loading()
else:
    print("No save found. Start a new game!")

show_menu()
start_game()