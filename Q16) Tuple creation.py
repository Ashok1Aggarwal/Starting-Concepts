#16. Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10). 
#    Write a program to perform following operations:
#           a. Print half the values of tuple in one line and the other half in the next line.
#           b. Print another tuple whose values are even numbers in the given tuple.
#           c. Concatenate a tuple t2=(11,13,15) with t1.
#           d. Return maximum and minimum value from this tuple.

t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
def printing():
    
    length = int(len(t1)/2)
    print(t1[:length])
    print(t1[length:])
def print_eve():
    another_tuple = []
    for i in range(len(t1)):
        if i%2 == 0:
            another_tuple.append(i)
        else:
            continue
    another_tuple = tuple(another_tuple)
    print(another_tuple)
def add_tuples_min_max():                  ##add, min and max value finder             
    t3 = t1+t2
    print("Newly made tuple names as t3 is : ", t3)
    l = len(t3)
    print("Minimum value in ", t3, "is : ", min(t3))
    print("Maximum value in ", t3, "is : ", max(t3))

print("""
#           a. Print half the values of tuple in one line and the other half in the next line.
#           b. Print another tuple whose values are even numbers in the given tuple.
#           c. Concatenate a tuple t2=(11,13,15) with t1 and return maximum and minimum value from this tuple.


""")
while True:
    x = input("Enter a choice : ")
    if x =='a':
        printing()
    elif x == 'b':
        print_eve()
    elif x == 'c':
        add_tuples_min_max()
    else:
        print("Your input ain't right, have a retry -__-")
        
add_tuples()



