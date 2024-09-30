"""
Hangman Text-Based Game
Kesiya Jacob
"""

import time
import random   # library that we use in order to choose random words from a list of words
import string

# lists contain list of words from each category that will be randomly selected
movies = ["up", "titanic", "hamilton", "joker", "interstellar", "coco", "frozen", "cinderella", "clueless", "mulan",
          "thor", "avatar", "it", "moana", "deadpool", "aquaman", "twilight", "shazam", "jaws", "cars", "superman",
          "bumblebee", "transformers", "tangled", "divergent", "maleficent", "jumanji", "brave", "ratatouille", "bambi",
          "aladdin", "elf", "matilda", "inception", "shrek", "ghostbusters", "pinocchio", "zootopia", "tarzan",
          "megamind", "godzilla", "coraline", "pocahontas", "benji", "annie", "paddington", "hugo", "madagascar",
          "wonder"]
countries = ["afghanistan", "albania", "argentina", "australia", "bangladesh", "belgium", "brazil", "bulgaria",
             "cambodia", "canada", "chile", "china", "croatia", "denmark", "ecuador", "egypt", "ethiopia", "finland",
             "france", "germany", "greece", "guinea", "haiti", "hungary", "iceland", "india", "indonesia", "iran",
             "iraq", "ireland", "israel", "italy", "jamaica", "japan", "kenya", "kuwait", "lebanon", "libya",
             "luxembourg", "madagascar", "malaysia", "mexico", "morocco", "nepal", "netherlands", "nigeria", "norway",
             "pakistan", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "singapore",
             "slovakia", "spain", "sweden", "switzerland", "syria", "thailand", "turkey", "ukraine", "uruguay",
             "venezuela", "vietnam", "yemen", "zimbabwe"]
fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple', 'cantaloupe', 'grapefruit', 'jackfruit', 'papaya',
          'watermelon', 'grapes', 'strawberry', 'blueberries', 'blackberries', 'kiwi', 'orange', 'raspberries', 'plum',
          'peach', 'nectarine', 'pomegranate']


def get_valid_word():  # function used to choose a random word for user to guess
    category = input("Which category would you like your word to be from (movies, countries, fruits): ").lower()
    while category != "movies" and category != "countries" and category != "fruits":
        print("Invalid entry!")   # error proofing
        category = input("Which category would you like your word to be from (movies, countries, fruits): ").lower()
    if category == "movies":
        word = random.choice(movies)  # randomly chooses a word from the list
        return word.upper()
    elif category == "countries":
        word = random.choice(countries)  # randomly chooses a word from the list
        return word.upper()
    elif category == "fruits":
        word = random.choice(fruits)  # randomly chooses a word from the list
        return word.upper()


def hangman():  # function where actual code for game is located
    word = get_valid_word()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters user has guessed

    lives = 7  # number of lives that user has

    while len(word_letters) > 0 and lives > 0:  # loop runs until all letters of word have been guessed or user has 0 lives left
        if lives == 7:
            print("                      ")
            print("\033[0;31;48mYou only have 7 lives to guess the word and save yourself from the monster! Good luck!")  # starting message of game, reminding user number of lives they have
            print("\033[0;36;48m------------")
            print("\033[0;36;48m|          |")
            print("\033[0;36;48m|           ")
            print("\033[0;36;48m|")
            print("\033[0;36;48m|")
            print("\033[0;36;48m|")
            print("\033[0;36;48m|")
        elif lives == 1:
            print("\033[0;31;48mYou only have", lives, "life left! Choose carefully!")  # specific message on last life
            print("\033[0;36;48m------------  ")
            print("\033[0;36;48m|          |  ")
            print("\033[0;36;48m|        \ O /")
            print("\033[0;36;48m|          |  ")
            print("\033[0;36;48m|         / \ ")
            print("\033[0;36;48m|")
            print("\033[0;36;48m|")
        else:
            print("\033[0;31;48mYou have", lives, "lives left!")  # printing the number of lives left for user
            if lives == 6:
                print("\033[0;36;48m------------  ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|          O ")
                print("\033[0;36;48m|            ")
                print("\033[0;36;48m|             ")
                print("\033[0;36;48m|")
                print("\033[0;36;48m|")
            elif lives == 5:
                print("\033[0;36;48m------------  ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|          O ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|            ")
                print("\033[0;36;48m|")
                print("\033[0;36;48m|")
            elif lives == 4:
                print("\033[0;36;48m------------  ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|          O ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|         /  ")
                print("\033[0;36;48m|")
                print("\033[0;36;48m|")
            elif lives == 3:
                print("\033[0;36;48m------------  ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|          O ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|         / \ ")
                print("\033[0;36;48m|")
                print("\033[0;36;48m|")
            elif lives == 2:
                print("\033[0;36;48m------------  ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|        \ O ")
                print("\033[0;36;48m|          |  ")
                print("\033[0;36;48m|         / \ ")
                print("\033[0;36;48m|")
                print("\033[0;36;48m|")
        # letters used
        # " ".join(["a", "b", "c", "d"]) --> "a b c d"
        print("\033[0;0;0mYou have used these letters so far: ", " ".join(used_letters))

        # what current word is (i.e. W _ R D)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("\033[0;32;48mCurrent word: ", " ".join(word_list))
        print("                                    ")

        # getting user input
        user_letter = input("\033[0;0;0mPlease enter a letter to guess the word: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)   # adding letter guessed to used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # removing letter guessed from letters in word

            else:
                lives = lives - 1  # takes away a life if guess is wrong
                print("                          ")
                print("The letter", user_letter, "is not in the word.")

        elif user_letter in used_letters:   # prints message if letter has already been guessed
            print("                 ")
            print("You have already guessed this letter. Please try again.")   # error proofing

        else:
            print("                     ")
            print("Invalid character. Please try again.")   # error proofing

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:  # user loses if lives == 0
        print("                    ")
        print("Oh no! You lost!")
        print("The hungry monster has gobbled you up!")
        print("\033[0;33;48mThe correct word was", word.upper())
        print("\033[0;0;0m                    ")
        answer = input("Would you like to play again (yes or no)? ")  # giving user option to play again
        if answer == "yes":
            hangman()
        else:
            print("                   ")
            print("Thanks for playing!")
            exit(0)  # ending program if user enters anything other than "yes"

    else:   # user wins if lives > 0 and all letters have been guessed
        print("                      ")
        print("\033[0;33;48mYay! You guessed the word", word.upper())
        print("\033[0;0;0mYou are saved from the hungry monster!")
        print("                    ")
        answer = input("\033[0;0;0mWould you like to play again (yes or no)? ")  # giving user option to play again
        if answer == "yes":
            hangman()
        else:
            print("                   ")
            print("Thanks for playing!")
            exit(0)   # ending program if user enters anything other than "yes"


name = input("Please enter your name: ")   # user enters their name first, followed by a welcome message
print("Welcome to Hangman, " + name + "!")
num = int(input("Please enter 1 for Instructions or 2 to Start Play: "))
while num != 1 and num != 2:
    print("Invalid entry!")   # error proofing
    num = int(input("Please enter 1 for Instructions or 2 to Start Play: "))
# printing out instructions
while num == 1:
    print("                            ")
    print("\033[0;35;48mInstructions")
    time.sleep(2)
    print("\033[0;0;0m1. Your goal is to guess the word to save yourself from the hungry monster.")
    time.sleep(2.5)
    print("2. Fill in the blanks by guessing one letter at a time on your keyboard to see if it’s in the word.")
    time.sleep(2.5)
    print("3. If you have guessed correctly, the letter will appear in the blank spaces.")
    time.sleep(2.5)
    print("4. Select a letter not in the word, you lose a life and a part of the “hangman” will appear!")
    time.sleep(2.5)
    print("5. You are only allowed 7 lives.")
    time.sleep(2.5)
    print(
        "6. Watch out - when all of the parts appear and you lose all of your lives, you’ll fall to the ground and "
        "be gobbled up by the hungry monster!")
    time.sleep(2.5)
    print(
        "7. Look at the blank spaces and try to guess the word, remember to keep the theme in mind – it may help "
        "you solve the puzzle!")
    print("                                      ")
    time.sleep(2.5)
    num = int(input("Please enter 1 for Instructions or 2 to Start Play: "))
# game begins
while num == 2:
    hangman()
