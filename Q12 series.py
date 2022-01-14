# 12) Write a function that finds the sum of the
#  a) till nth odd term
#  b) First nth even term
#  c) 1, 2, 4, 3, 5, 7, 9, 6, 8, 10, 11, 13.. till n-th term



def odd():
    sum = 0
    n = int(input("Enter the number of "))
    for i in range (0,n+1):
        if i%2 == 1 :
            sum += i
            print("term = ",i,", sum till this step = ", sum )
        else:
            continue

def even():
    n = int(input("Enter the number of "))
    sum = 0
    for i in range (0,n+1):
        if i%2 == 0 :
            sum+=i
            print("term = ",i,", sum till this step = ", sum )
        else:
            continue

odd()
even()