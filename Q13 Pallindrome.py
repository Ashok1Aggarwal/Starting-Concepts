#Write a Python function that takes a string as an input from the user and
# determines whether is it a palindrome or not

def pallindrome():
    str = input("Enter a string to check whether it's a palindrome or not  :  ")
    str = str.lower()
    length = len(str)-1
    for i in range(0,length):
        if  str[i] ==str[length]:
            length-=1
            print("string is a pallindrome :) ")
        else:
            print("string is not a pallindrome :( ")
while True:
        
    pallindrome()