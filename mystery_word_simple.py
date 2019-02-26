def guessed(mystery_word, letters_guessed):
    """
    Return True if all letters in mystery word have been guessed.
    """
    for letter in mystery_word.lower():
        if letter not in letters_guessed:
            return False
    return True


def letter_input(user_input):
    """
    Check to see if input is one character long and is a letter.
    """
    return len(user_input) == 1 and user_input.isalpha()


def get_letter_input():
    user_input = input("Type a letter to guess: \n").casefold()
    while not letter_input(user_input):
        print("Not a letter, please enter a letter.\n")
        user_input = input("Type a letter to make a guess: \n").casefold()
    
    return user_input


def get_display_word(mystery_word, letters_to_show):
    """
    Given the word being guessed and letters already guessed,
    display the word as a series of space-separated underscores (if the current
    has not yet been guessed) or current letter, uppercased.
    """
    output_chars = []
    for letter in mystery_word.lower():
        if letter in letters_to_show:
            output_chars.append(letter.upper())
        else:
            output_chars.append("_")

    return " ".join(output_chars)


def game_over(mystery_word, letters_guessed, guesses_left):
    return guessed(mystery_word, letters_guessed) or guesses_left == 0


if __name__ == "__main__":
    mystery_word = "tasmania"
    letters_guessed = []
    guesses_left = 8
    """
    Ask long as the entire word as not been guessed, the game will continue to ask for guesses.
    """
    while not game_over(mystery_word, letters_guessed, guesses_left):
        print(get_display_word,(mystery_word, letters_guessed))
        letter_guessed = get_letter_input()
        if letter_guessed in letters_guessed:
            print("That letter done been guessed.\n")
        elif letter_guessed in mystery_word:
            print("Correct! Nice guess.\n")
            letters_guessed.append(letter_guessed)
        else:
            letters_guessed.append(letter_guessed)
            guesses_left -= 1
            print(f"Try again. {guesses_left} more guess(es) remain(s). Choose wisely.\n")
            
            
    if guessed(mystery_word, letters_guessed):
        print(get_display_word,(mystery_word, letters_guessed))
        print("Winner winner!")
    else:
        print(f"The word was {mystery_word.upper()}.\n")
        print("Fool of a took. You lose.")

        