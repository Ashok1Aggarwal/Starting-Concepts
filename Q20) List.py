"""
20. Write a Python program to perform the following using list:
    a. Check if all elements in list are numbers or not
    b. If it is a numeric list, then count number of odd values in it
    c. If list contains all Strings, then display largest String in the list
    d. Display list in reverse form
    e. Find a specified element in list
    f. Remove the specified element"""


l=[]
n= int(input("Enter number of elements u want to add : "))
for i in range(n):
    x = int(input("Enter element you want to add : "))
    l.append(x)
print("Entered list is : ",l)

def checker_int(l):
    for i in range(0,len(l)):
        if l[i] == int:
            continue
        else:
            print("Checker found a non numeric value in the list -___-")
            break
    
def count_odd(l):
    cnt =0
    if checker_int(l) == True:
        for i in range(len(l)):
            if l[i]%2 ==1:
                cnt+=1
            else:
                continue
        print("Number of odd numbers in the provided list's : ", cnt)

def string_latgest(l):
    for i in range(0,len(l)):
        if l[i].isalpha()== True:
            print("Largest string in the list provided is : ",max(l))
        else:
            print("Checker found a non alpha value in the list -___-")

print(
""" a. Check if all elements in list are numbers or not
    b. If it is a numeric list, then count number of odd values in it
    c. If list contains all Strings, then display largest String in the list
    d. Display list in reverse form
    e. Find a specified element in list
    f. Remove the specified element"""
)
while True:
    fx = input("Enter a choice from above |^| : ")
    print('//////////////////////////////////////')
    if fx == 'a':
        checker_int(l)
    elif fx == 'b':
        count_odd(l)
    elif fx == 'c':
        string_latgest(l)
    elif fx == 'd':
        print("Input : ",l)
        print(reverse("output : ",l))
    elif fx == 'e':
        y = input("enter an element to search it in the list  : ")
        a = l.index(y)
        print("After searching the list we found indexes to be : ", a)
    elif fx == 'f':
        z = input("enter the element to be removed   : ")
        print("Previously inputed list is  : ",l)
        print("Item removed from  list is  : ",l.pop(z))
        print("Newely formatted   list is  :", l)
        continue

