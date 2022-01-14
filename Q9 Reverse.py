def reverse_n():
    n = int(input("Enter a number  : "))
    while (n>0):
        a = n % 10
        reverse = reverse * 10 + a
        n = n // 10
    print(reverse, "is the reverse of ",n)  
    
      
def sum_n():
    n = int(input("Enter a number  : "))
    sum =0
    while(n > 0):
        a = n % 10
        sum = sum + a
        n = n // 10

    print(sum, "is the sum of digits of ",n)

reverse_n()
sum_n()

