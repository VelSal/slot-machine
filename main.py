import random

#Global constants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

#Slot machine size
ROWS = 3
COLS = 3

symbolsCount = {
    "7" : 2 ,
    "*" : 4 ,
    "♫" : 6 ,
    "☺" : 8
}

#---------------------------------------------------------------|
#                                                               |
#                                                               |
'''
TO DO
def getSlotMachineSpin():
21:15 de la vidéo'''
#                                                               |
#                                                               |
#---------------------------------------------------------------|

#Function that asks for a deposit amount
def getDeposit():
    while True:
        depositInput = input("How much money to you want to deposit? ")
        if depositInput.isdigit():
            depositInput = int(depositInput)
            if depositInput > 0:
                break
            else:
                print("Please, deposit an amount greater than 0.")
                continue
        else:
            print("Please, enter a number greater than 0.")
            continue
    return depositInput

#Function to ask how many lines the user wants to bet on
def getNumberOfLines():
    while True:
        linesInput = input(f"How many lines to bet on? Choose from 1 to {MAX_LINES}. ")
        if linesInput.isdigit():
            linesInput = int(linesInput)
            #Verify that "lines" value is between 1 and MAX_LINES
            if 1 <= linesInput <= MAX_LINES:
                break
            else:
                print(f"Please, enter a valid number of lines. (between 1 and {MAX_LINES})")
                continue
        else:
            print("Please, enter a valid number.")
            continue
    return linesInput

#Function that asks how much money the user wants to bet
def getBet():
    while True:
        betInput = input(f"How much money do you want to bet on each line? Choose an amount between {MIN_BET} and {MAX_BET}. ")
        if betInput.isdigit():
            betInput = int(betInput)
            #Verify that the "bet" value is between MIN_BET and MAX_BET
            if MIN_BET <= betInput <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}€ and {MAX_BET}€")
                continue
        else:
            print("Please, enter a valid number.")
            continue
    return betInput

def main():
    balance = getDeposit()
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(f"You only have {balance}€ on your balance. Not enough to bet {totalBet}€.")
        else:
            break
    print(f"You are betting {bet}€ on {lines} lines for a total amount of {totalBet}€.")
    
main()