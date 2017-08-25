import string
import hangman as hng

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in letters_guessed:
        if letter in secret_word:
            return True
        else:
            return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = []
    for letter in secret_word:
        if letter in letters_guessed:
            word.append(letter)
        else:
            word.append('_ ')

    return ''.join(word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    list_of_letters = []
    string_of_letters = string.ascii_lowercase
    for letter in string_of_letters:
        if letter not in letters_guessed:
            list_of_letters.append(letter)
        else:
            None

    return ''.join(list_of_letters)

def secret_word():
    ''' 
    returns: string that is the selected word by the computer
    '''
    words = hng.wordlist
    computers_word = hng.choose_word(words)
    return computers_word

def input_check(user_input):
    str_user_input = ''.join(user_input)
    if str_user_input.islower() and str_user_input.isalpha():
        return True
    else:
        return False

