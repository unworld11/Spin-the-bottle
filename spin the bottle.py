import random
import time
import sys

print("Spin the Bottle ")

prc = int(input("Enter number of Participants : "))
l=[]
for i in range(prc):
    prc_name=input("Enter Name ")
    l.append(prc_name)

print("Starting the game")

ans = input("Are you readyy ??")
while ans =="yes" or ans=="Yes" or ans=="y":
    
    
          
    a=random.choice(l)
    print("Loading:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    print("The bottle points to ",a)
    ans = input("Another one ?? ")
    if ans =="yes" or ans=="Yes" or ans=="y":
        continue
    else:
        break
