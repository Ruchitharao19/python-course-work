'''#1
def addition(a,b):
    return a+b
num1=int(input())
num2=int(input())
result=addition(num1,num2)
print(result)
#2
def square(n):
    return n**2
#n=int(input())
print(square(7))
#3
def area(r):
    return 3.14*r*r
r=int(input())
print(area(r))
#4
def greet(name):
    print(f"Hello, {name}")
name=input("Enter your name:")
print(greet(name))
#5
def con(c):
    return (c*9/5)+32
    print(f"Temp
    erature in Fahrenheit:{f}")
c=float(input("Enter temperature in Celsius:"))
f=con(c)
print(f)
#6
def mul(a,b,c):
    return a*b*c
a=int(input())
b=int(input())
c=int(input())
print(mul(a,b,c))
#7
def simple_interest(p,t,r):
    si=(p*t*r)/100
    return si
p=float(input())
t=float(input())
r=float(input())
print(simple_interest(p,t,r))
#8
def length(s):
    count=0
    for i in s:
        count+=1
    return count
s="python"
print(length(s))

#9
l=list(map(int,input().split()))
double=list(map(lambda x: l.append[5],[0]))
print(double)              
#10
l=list(map(int,input().split()))
double=list(map(lambda i:l+i,l))
print(double)      
'''
#11
l=list(map(int,input().split()))
double=list(map(lambda i:sorted(l),l))
print(double)
def remove_ele(l,ele):
    l.remove(ele)
    return
l=list(map(int,input().split()))
print(remove_ele(1,3))
'''
def update(d):
    for i in d:
        d[i]+=1
    return d
d={'a':7,"b":4,'c':4}
print(update(d))

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(6))

n=int(input())
a,b,c=0,1,0
for i in range(n-2):
    c=a+b
    a=b
    b=c
print(c)

def factorial(n):
    fact = 0
    for i in range(1,n+1):
        fact=fact+i
    return fact
print(factorial(6))
