import random

gameIsOver=False

abc={
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

for key,value in abc.items():
    print(key,value)

#while the game is going on
while gameIsOver==False:
    row=input("Input row(a,b,c): ")
    pos=input("Input position(1,2,3): ")
    pos=int(pos)-1
    
    abc[row][pos]=playerCharacter
    for key,value in abc.items():
        print(key,value)
    gameIsOver=True

    
