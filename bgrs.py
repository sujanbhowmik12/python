"""rock=1
paper=-1
scissor=0"""

import random
computer = random.choice([1,-1,0])
print("Let's play ROCK_PAPER_SCISSOR:")
youdict={"r":1, "p":-1, "s":0}
youin=input("Enter your choice (r/p/s): ").lower()
revers = {1:"Rock", -1: "Paper", 0:"scissor"}
you = youdict[youin]
print(f"Your choice: {revers[you]} \ncomputer choice: {revers[computer]}")
if(computer == you):
    print("Game draw")
else:
    if(computer==-1 and you==1):
        print(":you win👍:")
    elif(computer==-1 and you==0):
        print(":you lose😒:")

    elif(computer==1 and you==-1):
        print(":you lose😒:")
    elif(computer==1 and you==0):
        print(":you win👍:")

    elif(computer==0 and you==1):
        print(":you lose😒:")
    elif(computer==0 and you==-1):
        print(":you win👍:")
        
    else:
        print("😂 Parbina channdu 🤣 🤣: ")

