import string
import hangman as hng
import hangman_functions as hngfnc



#secret_word = 'word'

def hangman():
    secret_word = hngfnc.secret_word()
    total_guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game of Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long")
    while total_guesses > 0 and warnings > 0:
        remaining_letters = hngfnc.get_available_letters(letters_guessed)
        print("------------------")
        print("You have " + str(warnings) + " warnings left")
        print("You have " + str(total_guesses) + " guesses left")
        print("Available Letters:" + remaining_letters)
        user_guess = input("Please guess a letter: ")
        user_input_check = hngfnc.input_check(user_guess)
        if user_guess in letters_guessed:
            warnings = warnings - 1
            print("Oops! You've already guessed that letter. You have " + str(warnings) + " warning(s) left")
            continue
        else:
            pass
        if not user_input_check:
            warnings = warnings - 1
            print("Oops! That is not a valid letter. You have " + str(warnings) + " warning(s) left")
            continue
        else:
            pass
        letters_guessed.append(str(user_guess))
        if user_guess in secret_word:
            result_guess = hngfnc.get_guessed_word(secret_word, letters_guessed)
            print("Good guess: " + str(result_guess))
        else:
            result_guess = hngfnc.get_guessed_word(secret_word, letters_guessed)
            print("Oops! That letter is not in my word: " + str(result_guess))
            if user_guess in ['a', 'e', 'i', 'o', 'u']:
                total_guesses = total_guesses - 2
            else:
                total_guesses = total_guesses - 1
        if hngfnc.is_word_guessed(secret_word, letters_guessed):
            total_score = (6 - total_guesses) * (len(set(secret_word)))
            print("Congratulations! You've Won! You da bes!")
            print("Damn son, your score is: " + str(total_score))
            break

    print("Game Over! You Lose! The word you needed to guess is: " + secret_word)