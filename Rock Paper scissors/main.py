import random
import sys
from enum import Enum 
class RPS(Enum):
    ROCK=1
    PAPER=2
    SISCORS=3


print(RPS(1).name)






def playerchoice():
    x=input("r for rock\n p for paper \n s for sissors ")
    return x
def Computerchoice():
    x=random.randint(1,3)
    if x==1:
        return "r"
    if x==2:
        return "p"
    if x==3:
        return "s"
    
def main():
    print("********* Rock Paper scissors ************")
    print("")
    x=playerchoice()
    print ("Your choice is "+x)

    y=Computerchoice()
    print(y)
    print ("the computrer choice  is "+y)

    match x:
        case "r":
            if(y=='r'):
                print("it a tie ")
            elif(y=='p'):
                print("you lose ")
            else:
                print("You won ")
        case "p":
            if(y=='p'):
                print("it a tie ")
            elif(y=='s'):
                print("you lose ")
            else:
                print("You won ")
        case "s":
            if(y=='s'):
                print("it a tie ")
            elif(y=='r'):
                print("you lose ")
            else:
                print("You won ")
if __name__=="__main__":
    playagain=1
    while playagain:
        main()
        playagain=int(input("1 continue 0 stop "))
    print("thank you for playing this game ")

