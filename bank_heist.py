from random import randint
from subprocess import call 
import os 

attempts = 5 # Change value to change number of guesses player gets
def welcome():
    print('''
                                Welcome to Bank Heist!!
                             _____________________________
                            |                             |
                            |   ||||||       |||    |||   |
                            |   |||  |||     |||    |||   |
                            |   |||  |||     |||    |||   |
                            |   ||||||       ||||||||||   |
                            |   |||  |||     |||    |||   |
                            |   |||  |||     |||    |||   |
                            |   |||||||      |||    |||   |
                            |_____________________________|

    Your mission is to rob the Greatest bank Ever to Built!! You will have %i attempts. 
         Get all of your attempts wrong and to jail you go ... For Life.

                Are you going to get rich? or Be locked up forever?
         
                                Let's Get Started!!!''' %attempts)
    
    print('''
                              You're holding up the bank.
                  The passcode will be total of %i digits long. 
                You must enter each number, from (0 - 9) one at a time.''' %code.length)

    print("\nTotal Attempts: %i" %attempts)
    print("**************************************")
def clear(): 
    call('clear' if os.name =='posix' else 'cls')
def goodbye():
    print('''
    Thanks for playing:
     ___________________________________________________________________________________________
    |                                                                                           |
    |   ||||||                               |||    |||                                     !!  |
    |   |||  |||                             |||    |||                                     !!  |
    |   |||  |||                kk           |||    |||                             tt      !!  |
    |   ||||||                  kk   k       ||||||||||    eee     ii     sssss    tttt     !!  |
    |   |||  |||  @@    nnnnnn  kk kk        |||    |||   ee ee    ii   sss         tt      !!  |
    |   |||  ||| @@ @   nn  nn  kkk          |||    |||  eeee      ii        sss     tt         |
    |   |||||||  @ @@@  nn  nn  kk  kk       |||    |||   eeeeee   ii    ssssss     tt      ::  |
    |___________________________________________________________________________________________|\n\n''')
class cipher:
    def __init__(self, length = 6):
        self.length = length #length is the passcode length
        cipher_code = []
        self.int = randint(0, 9)
        i = 0
        while i < length:
            cipher_code.append(self.int)
            i += 1
            self.int = randint(0, 9)
        self.cipher_code = cipher_code

code = cipher()
code_list = code.cipher_code

# Game
clear()
print(code_list) # *********  Prints code to be guessed  ************
welcome()
player_guesses = []
i = 0
code_list = ["__" for i in range(code.length)]  #Code_list displays code to screen for user
looping = True
for digit in code.cipher_code:  # Code.Cipher_code holds values for actual Code
    while looping:

# ---------------- Checking for a valid number to be entered --------------------
        check = True
        while check:
            try:
                guess = int(input("\nEnter Number (0 - 9):  "))
                if guess >= 0 and guess <= 9:
                    check = False
                else:
                    print("Please enter a number within the requested range.")
            except ValueError:
                print("Please enter a valid number.")

#  -------------- If KeyboardInterrrupt is ran, if statement will break loop -------------------
            except KeyboardInterrupt:
                print("\n\n\t\t----- Ending Game -----\n\n")
                looping = False
                break
        if looping == False:
            break

# ------------- Checking Player input against digits in code --------------------------------
        if guess == digit:
            attempts = 5
            print("-----------------------------")
            print("\n\t\tCorrect!!\n")
            print("Attempts Reset To: %i\n" %attempts)
            for num in range(len(player_guesses)):
                del player_guesses[0]
            code_list[i] = guess
            print(code_list)
            print("-----------------------------\n\n")
            i += 1
            if i == code.length:
                print("\tCongratulations!! You just became one rich person!")
                print("\t\tNow get out before the Cops come!!\n")
            break
        
        elif guess != digit:
            print("====================================")
            attempts -= 1
            for num in player_guesses:
                if guess == num:
                    print("You already entered %i. Please try a different number.\n" %guess)
                    attempts += 1
                    player_guesses.remove(guess)
                    continue
            player_guesses.append(guess)
            print("\n\t\tWRONG!!\n")
            print(("Attempts Remaining: %i" %attempts), "\tGuessed Numbers: ", player_guesses,"\n")
            print(code_list)
            print("====================================\n\n")

# --------------- Attempts Exhausted - Game Exits -----------------------------------------
        if attempts == 0:
            print("\t\tGame Over ... Looks like you're going to Jail.. Bye!!\n\n")
            looping = False
            break

# ----------  If game is won, attempts are exhausted, or KeyboardInterrupt is ran --- Breaking of loop continues -------------
    if i == code.length or attempts == 0 or looping == False:
        continue
   
    #     elif :
    #         play_again = input("Would you like to play again?: Yes(y) or No(n)\n")
    #         if play_again == "yes" or play_again == "y":
    #             valid = True
    #         else:
    #             valid = False
    # valid = False

goodbye()