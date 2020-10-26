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
#print(code_list) # *********  Printing code to be guessed  ************

print('''
                              You're holding up the bank.
                  The passcode will be total of %i digits long. 
                You must enter each number, from (0 - 9) one at a time.''' %code.length)

print("\nTotal Attempts: %i" %attempts)
print("**************************************")

# Game
valid = True
clear()
while valid:
    welcome()
    i = 0
    code_list = ["__" for i in range(code.length)]  #Code_list displays code to screen for user
    player_guesses = []
    looping = True
    for digit in code.cipher_code:  # Code.Cipher_code holds values for actual Code
        while looping:
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
                except KeyboardInterrupt:
                    print("\n\n\t\t----- Ending Game -----\n\n")
                    looping = False
                    break
            if looping == False:
                break
            if guess == digit:
                print("-----------------------------")
                print("\n\t\tCorrect!!\n")
                attempts = 5
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
                # looping = False
            
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

            if attempts == 0:
                print("\t\tGame Over ... Looks like you're going to Jail.. Bye!!\n\n")
                looping = False
                break
        if i == code.length or attempts == 0 or looping == False:
            continue
    valid = False
print('''
        Thanks for playing:
         ___________________________________________________________________________________________
        |                                                                                           |
        |   ||||||                               |||    |||                                     !!  |
        |   |||  |||                             |||    |||                                     !!  |
        |   |||  |||                kk           |||    |||                             tt      !!  |
        |   ||||||                  kk   k       ||||||||||    eee     ii     sssss    tttt     !!  |
        |   |||  |||  @@    nnnnnn  kk kk        |||    |||   ee ee    ii   sss         tt      !!  |
        |   |||  ||| @@ @   nn  nn  kkk          |||    |||  eeee      ii       sss     tt          |
        |   |||||||  @ @@@  nn  nn  kk  kk       |||    |||   eeeeee   ii   ssssss      tt      ::  |
        |___________________________________________________________________________________________|\n\n''')