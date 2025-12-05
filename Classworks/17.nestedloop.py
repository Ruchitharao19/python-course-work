
for row in range(5):
    for col in range(5):
        print(row,end=" ")
    print()

for row in range(5):
    for col in range(5):
        print(col,end=" ")
    print()
    
for row in range(5):
    for col in range(row+1):
        print(col,end=' ')
    print()

n=int(input())
for row in range(n):
    for col in range(n-row):
        print(col,end=' ')
    print()

n=int(input())
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print("*",end=' ')
    print()

n=int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or (row==n-1) or (col==n-1):
            print('*', end=' ')
        else:
            print(" ",end=' ')
    print()

n=int(input())
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or (row==n-1) or (col==n-1) or row==n//2:
            print('*', end=' ')
        else:
            print(" ",end=' ')
    print()

n=int(input())
for row in range(n):
    for col in range(n):
        if row==0 or (row==n-1) or row+col==4:
            print('*', end=' ')
        else:
            print(" ",end=' ')
    print()

n=int(input())
for row in range(n):
    for col in range(n):
        if row==col or col==row  or :
            print('*', end=' ')
        else:
            print(" ",end=' ')
    print()

n=int(input())
for row in range(n):
    for col in range(n):
        if j%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        if i<j:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range(n):
        if i==n//2 or(j==0 and i>n//2) or (j==n-1 and i>n//2) or (i+j==n//2 or j-i==-n//2) and i<n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   
#list inside list
l=[[1,2,3],[4,5,6],[7,8]]
for i in l:
    for j in i:
        print(j)
l=[[1,2,3],[4,5,6],[7,8]]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])
#tuple inside tuple(nestedtuple)
t=((1,2),(3,4),(5,6))
for i in t:
    for j in i:
        print(i,j)
#nested dictionary
data={
    'apple':{'price':50,'discount':5},
    'mango':{'price':100,'discount':10},
    'papaya':{'price':150,'discount':7},
    'banana':{'price':30,'discount':0},
    }
for i in data:
    for j in data[i]:
        print(i,j,data[i][j])

