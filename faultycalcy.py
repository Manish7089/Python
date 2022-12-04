while(1):
    print("enter two numbers ")
    n1 = int(input())
    n2 = int(input())
    # print("what operation you perform : ")
    # o1=input()
    o1 = input("what operation u need to perform :")
    if o1 == "+":
        if n1 == 56 and n2 == 9:
            print("77")
        else:
            print("Sum is : ", n1 + n2)
    elif o1 == "*":
        if n1 == 45 and n2 == 3:
            print("555")
        else:
            print("Multiplication :", n1 * n2)
    elif o1 == "/":
        if n1 == 56 and n2 == 6:
            print("4")
        else:
            print("Division :", n1 / n2)
    elif o1 == "-":
        print("Sub :", n1 - n2)
    elif o1 == "**":
        print("n1 power n2 :", n1 ** n2)
    m=input("if u want perform again type Y and N for not ")
    if m=='Y' or m=='y':
        continue
    else:
        print("thanks for using calculator...")
        break
