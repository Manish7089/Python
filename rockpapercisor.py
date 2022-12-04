import random
print("......Rock Paper Scissors game......")
uthrow=input("Your throw :")
op=["Rock","Paper","Scissor"]
pthrow=random.choice(op)
print("Computer's throw :",pthrow)

if uthrow==pthrow:
    print("Tie")
elif uthrow=="Rock" and pthrow=="Scissor":
    print("You Win.")
elif uthrow=="Rock" and pthrow=="Paper":
    print("You lose.")
elif uthrow=="Paper" and pthrow=="Scissor":
    print("You lose.")
elif uthrow=="Paper" and pthrow=="Rock":
    print("You lose.")
elif uthrow=="Scissor" and pthrow=="Paper":
    print("You Win.")
elif uthrow=="Scissor" and pthrow=="Rock":
    print("You lose.")