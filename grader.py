while True:
    a = int(input("enter your marks  : "))
    if a>=90 and a<= 100:
        print("excellent")
    elif 80<=a and a<=90:
        print("A")
    elif 80>=a and 70<=a:
        print("B")
    elif 60<=a and 70>=a:
        print("C") 
    elif 50<=a and 60>=a:
        print("D")        
    else:
        print("very poor")