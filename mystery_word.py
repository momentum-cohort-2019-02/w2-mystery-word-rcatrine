import random, sys

wordList = ["drink", "window", "apple", "chair", "bed"]

guess = []
# Select random word from list
selected_word = random.choice(wordList)
word_length = len(selected_word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_list = []



def start_game():
    print("Hi there!")

    while True:
        name = input("What is your name?\n").strip()
        break

start_game()



def start_prompt():
    print("Time to play!")

    while True:
        start_choice = input("Ready to start? Please enter yes or no in lowercase.\n")

        if start_choice == "yes":
            break
        elif start_choice == "no":
            sys.exit("Ok, another time then.")
        else:
            print("Please enter yes or no in lowercase.")
            continue

start_prompt()



def word_select():

    # Create blank space template for each letter of every word in list
    for letter in selected_word:
        guess.append("_")

        print("The word in question has", word_length, "letters.")

        print("You may only enter 1 lowercase letter of the alphabet at a time.\n")

        print(guess)


def print_word_to_guess(letters):
    """Utility function to print the current word to guess"""
    print("Word to guess: {0}".format(" ".join(guess)))


def letter_guess():
    guess_count = 1

    while guess_count < 8:


        guess_choice = input("Pick a letter\n").lower()

        # Redirect if user enters something other than a lowercase letter
        if not guess_choice in alphabet:
            print("Please enter a lowercase letter from a to z.")
        elif guess_choice in letter_list:
            print("Letter has already been guessed.")
        else:

            letter_list.append(guess_choice)
            if guess_choice in selected_word:
                print("Bingo. Nice job!")
                for x in range(0, word_length):
                    if selected_word [x] == guess_choice:
                        guess[x] == guess_choice
                print(guess)
                    
                if not "_" in guess:
                    print("Congrats, you won!")
                    break
                else:
                    print("Incorrect, try again.")
                    guess_count += 1
                    if guess_count == 8:
                        print("Sorry, you ran out of guesses, game over. The secret word was", selected_word)


word_select()
letter_guess()

print("Game over.")


if __name__ == "__main__":
    start_game()
    start_prompt()
    word_select()
    letter_guess()


#___________________________________________________________________________
# Mystery Word with imported list of words

# list = open('words.txt').read().replace('\n', ', ')
# new_list = []
# new_list.append(list)
# print (new_list)



# easy_words = []
# medium_words = []
# hard_words = []
# for word in list:                  
#     if len(word) >= 4 and len (word) <= 6:
#         easy_words.append(word)
        
#     if len(word) >= 6 and len(word) <= 8:
#         medium_words.append(word)

#     if len(word) >= 8: 
#         hard_words.append(word)



# def difficulty_choice(Easy, Medium, Hard):
#     if difficulty_choice = Easy
#         print("Easy Mode")
#         elif difficulty_choice = Medium
#         print("Medium Mode")
#         elif difficulty_choice = Hard
#         else: print("Hard Mode")








