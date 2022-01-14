## Write a Python function that prints a dictionary where the keys are numbers
# between 1 and 5 and the values are cubes of the keys

d=dict()
for x in range(1,5+1):
    d[x]=x**3
print(d)  