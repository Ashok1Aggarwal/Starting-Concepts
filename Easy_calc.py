# Calculator
x = 0
while x<1:
    n1 = int(input("Enter first number   :  "))
    n2 = int(input("Enter second number  :  "))
    a = input("enter your choice  : ")
    y = int(input("Enter number of opera"))
    if a == '+':
        print("The Sum is        : ",n1+n2)
    elif a == '-':
        print("The Difference is : ", n1-n2)
    elif a == '*':
            print("The Product is    : ", n1*n2)
        elif a == "/":
            print("The Division is   :", n1/n2)
        else:
            print("wrong Imput")


