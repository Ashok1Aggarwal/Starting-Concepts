#17. 
# Write a function called “check_duplicates” that takes a list and returns true if
# there is any element that appears more than once. Also find the frequency of that
# element. The original list should not be modified.

def check_duplicates():
    l = []
    l2 = []
    n = int(input("Please enter the number of elements you wish to add to the list  :  "))
    for i in range(n):
        x = int(input("Enter element  :"))
        l.append(x)
    print("Your entered list is : ", l )

    for i in range(n):
        if l[i] not in l2:
            l2.append(i)
        else:
            print("element repeated is : ", i)


check_duplicates()

