'''#1
n=int(input())
for i in range(1,n+1):
    print(i)
#2
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i)
#3
n=int(input())
total=0
for i in range(1,n+1):
    total+=i
print(total)
#4
n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        print(i)
#5
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
#6
n=int(input())
res=0
for i in range(1,11):
    res=n*i
    print(f"{n}*{i}= {res}")
    
#7
n=int(input())
if n<=1:
    print(n,"is not a prime")
else:
    is_prime=True
    for i in range(1,n):
        if i%2==0:
            is_prime=False
            break
    if is_prime:
        print(n,"is a prime")
    else:
        print(n,"is a prime")
        
#8
n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    digit = n % 10         
    sum_digits += digit    
    n = n // 10       t
print("Sum of digits =", sum_digits)
#9
n=int(input())
a=0
b=1
for i in range(n):
    print(a, end=' ')
    c=a+b
    a,b=b,c
    
#10
n=int(input())
res=0
for i in range(1,n+1):
    if i%3==0:
        res+=1
print(res, end=' ')

#11
#12
n=int(input())
res=0
for i in range(5,n+1):
    if i%5==0:
        print(i, end=" ")
 '''       

