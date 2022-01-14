"""19. Write a menu driven program to perform the following functions on strings:
a. Find the length of string
b. Return maximum of three strings
c. Accept a string and replace every successive character with ‘#’ 
   ExampleFor Given string ‘Hello World’ returned string is ‘H#l#o W#r#d’.
d. Find number of words in the given string"""


def lenght(str):
    l = len(str)
    print("Length of inputed string is : ",l)
def changer_hash(str):
    str2 = ''
    for i in range(0, len(str)):
        if str[i] == ' ':
            str2+= ' '
        elif i%2 == 0:
            str2+= str[i]
        else:
            str2+= '#'
    print(str2)
def counter(str):
    s = str.split()
    l = len(s)
    print("number of words in the given string are : ", l)


print("""
a. Find the length of string
b. Return maximum of three strings
c. Accept a string and replace every successive character with ‘#’ 
d. Find number of words in the given string""")
str = input("Kindly enter a string : ")
while True:
    x = input("Enter a choice :) : ")
    
    if x =='a':
        lenght(str)
    elif x =='c':
        changer_hash(str)
    elif x =='d':
        counter(str)      
    else:
        print("You gotta pay attention, here have another try -___- ")  
