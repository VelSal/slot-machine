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
    "☺" : 8 ,
}

symbolsValue = {
    "7" : 5 ,
    "*" : 4 ,
    "♫" : 3 ,
    "☺" : 2 ,
}

def getWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else: 
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
    return winnings, winningLines

#Function that generate the symbols in the columns 
def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol , symbolsCount in symbols.items():
        for _ in range(symbolsCount):
            allSymbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        #Copying the allSymbols list 
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
            
        columns.append(column)
    
    return columns

#Function that flips the columns to make them vertical
def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row] , end=" | ")
            else:
                print(column[row], end="")
        
        #Printing a newline
        print()
        
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

def spin(balance):
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(f"You only have {balance}€ on your balance. Not enough to bet {totalBet}€.")
        else:
            break
    print(f"You are betting {bet}€ on {lines} lines for a total amount of {totalBet}€.")
    
    slots = getSlotMachineSpin(ROWS, COLS, symbolsCount)
    printSlotMachine(slots)
    winnings, winningLines = getWinnings(slots, lines, bet, symbolsValue)
    print(f"You won {winnings}€.")
    print(f"You won on lines:", *winningLines)
    return winnings - totalBet

def main():
    balance = getDeposit()
    while True:
        print(f"Current balance is {balance}€")
        play = input("Press enter to play or q to quit. ")
        if play == "q":
            break
        balance += spin(balance)
        
    print(f"You left with {balance}€")
        
    
main()
