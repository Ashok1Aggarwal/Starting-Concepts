def square():
    x = int(input("Enter a side of the building  : "))
    print("Area of building is  : ", x*x)
def rectangle():
    l = int(input("Enter Length of the buliding   : "))
    b = int(input("Enter Breadth of the building  : "))
    print("Area of the building is                :  ", l*b)
def circle():
    r = int(input("Enter the radius of building   : "))
    print("Area of the building is                : ",3.14*(r**2) )

print("what is the shape of bulding? ")
print("1) Square? ")
print("2) Rectangle? ")
print("3) Circle? ")

while True:
    choice = int(input("Enter your choice  : "))
    if choice == 1:
        square()
    elif choice == 2:
        rectangle()
    elif choice == 3:
        circle()
    else:
        print("Check the options again and retry : ")
        continue
