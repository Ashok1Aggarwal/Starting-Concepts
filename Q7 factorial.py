while True:
    product = 1
    n = int(input("Enter the number of which u need factorial  : "))
    if n<0:
        print("please only enter a negative number -_- ")
    else:
        for i in range(1,n+1):
            product = product*i
        print(product)