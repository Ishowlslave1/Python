import random

gameIsOver=False

pole={
    "a":['-','-','-'],
    "b":['-','-','-'],
    "c":['-','-','-'],
}

print("Welcome to the TicTacToe game!")

#let the player decide which character will he use 
playerCharacter=input("Choose your character(o,x): ")
if playerCharacter=="o":
    computerCharacter="x"
if playerCharacter=="x":
    computerCharacter="o"

for key,value in pole.items():
    print(key,value)

#while the game is going on
while gameIsOver==False:

    #player's move
    pl_row=input("Input row(a,b,c): ")
    pl_col=input("Input position(1,2,3): ")
    pl_col=int(pl_col)-1
    pole[pl_row][pl_col]=playerCharacter

    #printing updated pole
    def printPole():
        for key,value in pole.items():
            print(key,value)
    printPole()

    #printing separator
    for counter in range(1,20):
        print("-",end="")
    print("")
    
    #computer chooses position
    comp_row=random.choice(["a","b","c"])
    comp_col=random.randint(1,3)
    comp_col=comp_col-1

    while pole[comp_row][comp_col]==playerCharacter:
        comp_row=random.choice(["a","b","c"])
        comp_col=random.randint(1,3)
        if pole[comp_row][comp_col]!=playerCharacter:
            break
    pole[comp_row][comp_col]=computerCharacter
    
    #printing updated pole
    printPole()

    #checking who has won
    #checking diagonals
    if pole["a"][0]==playerCharacter and pole["b"][1]==playerCharacter and pole["c"][2]==playerCharacter:
        print("You win!")
        gameIsOver=True
    if pole["a"][0]==playerCharacter and pole["b"][1]==playerCharacter and pole["c"][2]==computerCharacter:
        print("You have lost!")
        gameIsOver=True
    if pole["a"][2]==playerCharacter and pole["b"][1]==playerCharacter and pole["c"][0]==playerCharacter:
        print("You win!")
        gameIsOver=True
    if pole["a"][2]==computerCharacter and pole["b"][1]==computerCharacter and pole["c"][0]==computerCharacter:
        print("You have lost!")
        gameIsOver=True
        
    #checking vertical lines
    if pole["a"][0]==playerCharacter and pole["b"][0]==playerCharacter and pole["c"][0]==playerCharacter:
        print("You win!")
        gameIsOver=True
    if pole["a"][1]==playerCharacter and pole["b"][1]==playerCharacter and pole["c"][1]==playerCharacter:
        print("You win!")
        gameIsOver=True
    if pole["a"][2]==playerCharacter and pole["b"][2]==playerCharacter and pole["c"][2]==playerCharacter:
        print("You win!")
        gameIsOver=True

    if pole["a"][0]==computerCharacter and pole["b"][0]==computerCharacter and pole["c"][0]==computerCharacter:
        print("You have lost!")
        gameIsOver=True
    if pole["a"][1]==computerCharacter and pole["b"][1]==computerCharacter and pole["c"][1]==computerCharacter:
        print("You have lost!")
        gameIsOver=True
    if pole["a"][2]==computerCharacter and pole["b"][2]==computerCharacter and pole["c"][2]==computerCharacter:
        print("You have lost!")
        gameIsOver=True
    
    #checking horizontal lines
    if pole["a"][0]==playerCharacter and pole["a"][1]==playerCharacter and pole["a"][2]==playerCharacter:
        print("You win!")
        gameIsOver=True
    if pole["b"][0]==playerCharacter and pole["b"][1]==playerCharacter and pole["b"][2]==playerCharacter:
        print("You win!")
        gameIsOver=True
    if pole["c"][0]==playerCharacter and pole["c"][1]==playerCharacter and pole["c"][2] == playerCharacter:
        print("You win!")
        gameIsOver=True

    if pole["a"][0]==computerCharacter and pole["a"][1] and pole["a"][2]==computerCharacter:
        print("You have lost!")
        gameIsOver=True
    if pole["b"][0]==computerCharacter and pole["b"][1]==computerCharacter and pole["b"][2]==computerCharacter:
        print("You have lost!")
        gameIsOver=True
    if pole["c"][0]==computerCharacter and pole["c"][1]==computerCharacter and pole["c"][2]==computerCharacter:
        print("You have lost!")
        gameIsOver=True

playAgain=input("Would you like to play again?(yes,no): ")
if playAgain == "yes" or playAgain == "YES" or playAgain == "Yes":
    gameIsOver=False

print("<Press enter to exit>")
input()
