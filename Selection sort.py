list1=[3,5,2,57,87]
n=len(list1)
for i in range(0,n):
    small=list1[i]
    pos=i
    for j in range(i+1,n):
        if list1[j]>small:
            small=list1[j]
            pos=j
            list1[pos]=list1[i]
            list1[i]=small
print(list1)
