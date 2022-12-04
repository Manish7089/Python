n=30
print("guess the num between 1 to 50")
print("you have only 9 chances ..")
for i in range(9):

    estimated=int(input("Guess the number :"))
    if estimated>n:
        print("estimation is higher...guess the lower")
     #   i += 1
        print("chance left ", 9 - (i + 1))
    elif estimated<n:
        print("estimation is lower...guess the higher")
      #  i += 1
        print("chance left ", 9 - (i + 1))
    else:
        print("Your guess is correct.YOU WON...")
        print("your attempt :", i+1)
        break
    if (i>=8):
        print("Game Over..")


#   continue

