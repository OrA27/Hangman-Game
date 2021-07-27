# this is my project for the hangman game
# course of the program worded


# print the title along with how many tries player has
# function hangman_title
# requires having amount of tries entered beforehand
# DONE

# while play != 'n'
# if play != y
# error
# add playing variable
# DONE

# ask player to enter file path and an index number for a word
# function choose_word
# this will give the secret word
# function file_exist
# DONE

# clear the screen
# needs to import os and use os.system('cls')
# DONE

# start a while loop for amount of tries > 0
# Done

# inside it start another while loop for winning
# function check win true or false
# Done

# show tries, the hangman state and under it the secret word, unrevealed
# "you have %d tries remaining" %(tries - 1)
# function print_hangman
# # there are 7 states but 6 tries
# function show_hidden_word
# # requires having an old_letters list beforehand


# request from player to guess a letter
# function check_valid_input
# if valid input true
# function try_update_letter
# and continue
# if valid input false
# notify player of error and return to guess a letter


# function try update = true                                # function try update = false
# clear screen and return to line 21                        # deduct 1 from tries
# return to line 21

# amount of tries = 0 and check win = False                 # amount of tries > 0 and check win == True
# clear screen                                              # clear screen
# print "you lose"                                          # print "you win"


# ask if player wants to play again
# if play = y   # if play = n
# rerun         # exit
# if play != y\n
# ask again
import os
import time


def win_lose(result):
    """prints the result of the game
    :param result: result of game
    :type result: int
    :return: None"""
    result_dict = {0: """
____    ____  ______    __    __     ____    __    ____  __  .__   __.     __  
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  |    |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  |    |  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  |    |  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   |    |__| 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__|    (__) 

""",
                   1: """
____    ____  ______    __    __      __        ______        _______. _______     __  
\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____|   |  | 
 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__      |  | 
  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|     |  | 
    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____    |__| 
    |__|     \______/   \______/     |_______| \______/  |_______/    |_______|   (__) 

"""}
    print(result_dict[result])


def sequence_del(my_list):
    # this is a "sub-function" for the
    # "choose_word" function" from exercise 9.4.1
    """takes a list of random words and remove all duplicates
    :param my_list: user list
    :type my_list: list
    :return: a list without duplicates
    :rtype: list"""
    new_list = []  # empty list for end result
    for word in my_list:  # check each word in list
        if word not in new_list:
            new_list.append(word)  # add word to new list
    return new_list  # return the new list


def hangman_title(with_num_tries):
    """prints the title of the hangman game
    and how many tries the player has
    :param with_num_tries: how many tries the player has
    :type with_num_tries: int
    :return: None"""
    # title of game
    TITLE = ("""
 _   _    ___    _   _   _____  ___  ___   ___    _   _ 
| | | |  / _ \  | \ | | |  __ \ |  \/  |  / _ \  | \ | |
| |_| | / /_\ \ |  \| | | |  \/ | .  . | / /_\ \ |  \| |
|  _  | |  _  | | . ` | | | __  | |\/| | |  _  | | . ` |
| | | | | | | | | |\  | | |_\ \ | |  | | | | | | | |\  |
\_| |_/ \_| |_/ \_| \_/  \____/ \_|  |_/ \_| |_/ \_| \_/
\n\t""")

    print(TITLE, with_num_tries, "\n")  # print title and tries


def choose_word(file_path, index):
    # this is the function for exercise 9.4.1
    """chooses a random word for a text file
    and say how many different words are in the file
    :param file_path: location of text file
    :param index: index of the word chosen by the user (starts from 1)
    :type file_path: str
    :type index: int
    :return: chosen word and how many
        different words are in the text
    :rtype: tuple"""
    with open(file_path, 'r') as bunch_of_words:  # open the file
        middle_man = bunch_of_words.read()  # use extra value for code understanding
        words_list = middle_man.split(' ')  # create a list of words from text file

    num_of_words = len(words_list)  # amount of words in file
    real_index = index - 1  # the real index of the word
    while real_index > num_of_words:  # in case real index is bigger than the amount of words
        real_index -= num_of_words  # remove the amount of words until a viable number appears

    word_of_choice = words_list[real_index]  # this is the chosen word
    improved_list = sequence_del(words_list)  # remove all duplicate using sub_function
    different_words = len(improved_list)  # amount of different words in the list
    result = (different_words, word_of_choice)  # resulting tuple

    return result


def file_exist(file_path):
    """checks if a file exists.
    :param file_path: path of file
    :type file_path: str
    :return: none"""
    if os.path.isfile(file_path):  # use isfile()
        return True
    else:
        return False


def check_win(secret_word, old_letters_guessed):
    # function made for exercise 7.3.2
    """checks if the secret word can be made from the letters
    guessed beforehand
    :param secret_word: the word needed to guess by player
    :param old_letters_guessed: letters that were already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: partial view of the secret word
    :rtype: bool"""
    # create new string to be used as result
    win = ""
    # check each letter in the word
    for letter in secret_word:
        # check if said letter is in the list
        if letter in old_letters_guessed:
            # add a letter
            win += "w"
        # in case the secret word contains spaces
        elif letter == " ":
            # add a letter
            win += "w"
        else:
            # if letter not included, leave an underscore
            win += "_"
    # check if all characters in win are letters
    if win.isalpha():
        return True
    else:
        return False


def print_hangman(num_of_tries):
    # this function is made for exercise 8.4.1
    """prints state of hangman in correlation
    with number of tries
    :param num_of_tries: how many tries left
    :type num_of_tries: int
    :return: None"""
    # "image" dictionary
    hangman_photos = {6: """x-------x\n\n\n\n\n""",
                      5: """x-------x
|
|
|
|
|""",
                      4: """x-------x
|       |
|       0
|
|
|""",
                      3: """x-------x
|       |
|       0
|       |
|
|""",
                      2: """x-------x
|       |
|       0
|      /|\\
|
|""",
                      1: """x-------x
|       |
|       0
|      /|\\
|      /
|""",
                      0: """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}
    # check if dictionary key is the same as the parameter
    for pic in hangman_photos:
        if pic == num_of_tries:
            print(hangman_photos[pic])  # print selected "image"


def show_hidden_word(secret_word, old_letters_guessed):
    # function made for exercise 7.3.1
    """shows a partial part of the secret word
    with the old letters guessed shown and the rest hidden
    :param secret_word: the word needed to guess by player
    :param old_letters_guessed: letters that were already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: partial view of the secret word
    :rtype: str"""
    # create new string to be used as result
    hidden_word = ""
    # check each letter in the word
    for letter in secret_word:
        # check if said letter is in the list
        if letter in old_letters_guessed:
            # add a letter with a space for easier understanding
            hidden_word += letter + " "
        else:
            # if not, leave an underscore with a space
            hidden_word += "_ "
    return hidden_word


def check_valid_input(letter_guessed, old_letters_guessed):
    # this is the function for exercise 6.4.1
    """checks if the letter guessed is valid and if it was
    guessed before.
    :param letter_guessed: a letter that was guessed by user.
    :param old_letters_guessed: consists all letters that were
    already guessed in lower case only.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return if input was a single letter or was guessed before.
    :rtype: bool"""
    # turn any input into string
    new_guess = str(letter_guessed)
    # check length of string
    guess_length = len(new_guess)
    # check if string is alphabetic
    alphabetic = new_guess.isalpha()
    # check wanted conditions: single letter and not guessed
    if (guess_length == 1 and alphabetic) and \
            letter_guessed.lower() not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    # this is the function for exercise 6.4.2
    """checks if letter was guessed before or not.
    :param letter_guessed: a letter that was guessed by user.
    :param old_letters_guessed: consists all letters that were
    already guessed in lower case only.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: if letter can (and will) be added to list
    :rtype: bool"""
    # turn any input to string
    new_guess = str(letter_guessed)
    # check length of string
    guess_length = len(new_guess)
    # check if string is alphabetic
    alphabetic = new_guess.isalpha()
    # check several conditions and respond to them:
    if (guess_length == 1 and alphabetic) and letter_guessed.lower() \
            not in old_letters_guessed:
        # add new guess to list and return True
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        old_letters_guessed.sort()
        list_to_string = '-> '.join(old_letters_guessed)
        print(" X\n", list_to_string.strip())
        return False


def sleep_clear(sec):
    """pauses the program and then clears screen
    :param sec: amount of time for pausing program
    :type sec: float
    :return: none"""
    time.sleep(sec)
    os.system('cls')


def main():

    # replay block

    want_to_play = 'y'

    while want_to_play != 'n':  # begin the game

        if want_to_play != 'y':  # in case input is wrong
            want_to_play = input("please enter a correct option y\\n:\n\t")

    # -----------------------------------------------------------------------------------------------------------------
        # game title and initial values block

        elif want_to_play == 'y':  # player wants to play
            hm_states = 6
            letters_guessed = []
            hangman_title(hm_states)  # print the title of game and tries

            # ---------------------------------------------------------------------------------------------------------
            # file entry and check if file exists

            file_path = input("please enter the path file of your text:\n")
            is_file = file_exist(file_path)  # run if file exists

            while not is_file:
                # if file path is wrong enter it again
                file_path = input("file not found, please enter different path:\n")
                # get new value of file_path
                is_file = file_exist(file_path)

            # ---------------------------------------------------------------------------------------------------------
            # word index entry and check if its an actual number

            word_index = input("please enter a number to choose a word:\n")  # index of word chosen
            while not word_index.isnumeric():  # check word_index is a number
                word_index = input("please enter a number to choose a word:\n")

            # ---------------------------------------------------------------------------------------------------------
            # word extraction and choosing from file

            num_and_word = choose_word(file_path, int(word_index))  # get word and how many different words in file
            the_word = num_and_word[1].lower()  # get only the word
            os.system('cls')  # clear screen

            # ---------------------------------------------------------------------------------------------------------
            # game-play block

            # as long as the player has less than 6 mistakes
            # and
            # as long as the player didn't find the word
            # condition block for win or lose
            while hm_states > 0 and not check_win(the_word, letters_guessed):
                # display stats of player

                print("you have {} tries left".format(hm_states))  # show tries
                print_hangman(hm_states)  # show state of hangman
                print("OOOOOOOOOO\n /\\ /\\ /\\ \n")  # floor for gallows
                print(show_hidden_word(the_word, letters_guessed))  # show the word (partially) hidden
                new_letter = input("guess a letter:\t")  # request a letter from player
                # ----------------------------------------------------------------------------------------
                # assign value for function

                valid = check_valid_input(new_letter, letters_guessed)
                was_not_guessed = try_update_letter_guessed(new_letter, letters_guessed)
                # ----------------------------------------------------------------------------------------
                # letter check

                if valid and was_not_guessed:
                    # for correct letters that were'nt guessed
                    if new_letter in the_word:
                        print("correct!")
                        sleep_clear(0.75)

                    # for wrong letters that were'nt guessed
                    elif new_letter not in the_word:
                        print("wrong :(")
                        hm_states -= 1  # reduce tries by 1
                        sleep_clear(0.75)

                # for guessed letters and invalid characters
                else:
                    # increase sleep time as more letters were guessed
                    print("character invalid or letter was already guessed")
                    sleep_clear(1 + (len(letters_guessed)) * 0.75)
                    continue
                # ------------------------------------------------------------------------------------------
                # win\lose conditions fulfilled
            else:
                # win condition

                if check_win(the_word, letters_guessed):
                    os.system('cls')
                    win_lose(0)
                # --------------------------------------
                # lose condition

                elif hm_states == 0:
                    print_hangman(hm_states)
                    print("OOOOOOOOOO\n /\\ /\\ /\\ \n")  # floor for gallows
                    win_lose(1)
                # --------------------------------------

        # replay block

        want_to_play = input("would you like to play again y/n:\t")
        os.system('cls')


if __name__ == '__main__':
    main()
