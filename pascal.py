n = int(input("enter the row number:"))
list1 = []
for i in range(n):
    list=[]#created a temporary list
    for j in range(i+1):
        if j == 0 or j == i:
            list.append(1)
        else:
            list.append(list1[i-1][j-1] + list1[i-1][j])# current row will be i, we have to take sum of two numbers in previous row
    list1.append(list)


for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(list1[i] [j], end=" ")
    print()