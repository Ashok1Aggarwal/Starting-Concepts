# Bubble sorting a user defined list

list1=[]
n=int(input("enter no of elements : "))
for i in range(0,n):
    x=int(input("enter element : "))
    list1.append(x)
for i in range(0,n):
    for j in range(0,n-i-1):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print(list1)
