### The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
def Fibonacci_number():
    n = int(input("enter number till which u want the series   :  "))
    x,y = 0,1
    if n < 0 :
        print("Only Positive numbers allowed -_- ")
    elif n ==x:
        print(x)
    elif n > x:
        print(x, end='  ')
        for i in range(2, n+1):
            z = x+y
            x = y
            y = z
            print(y, end='  ')

        


Fibonacci_number()


