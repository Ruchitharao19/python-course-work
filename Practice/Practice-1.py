#10,6
'''
#1
a,b,c= tuple(map(int, input().split(",")))
if a==b and b==c and a==c:
    print("equalateral triangle")
elif a!=b and b!=c and a!=c:
    print("scalen triangle")
else:
    print("isosceles triangle")


#2
ch=input()
var="aeiouAEIOU"
if ch in var:
    print("vowles")
elif ch.isalpha():
    print("consonents")
elif ch.isdigit():
    print("digit")
else:
    print("special character")

#3
height=float(input())
weight=float(input())
bmi=weight/(height*height)
if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<=24.9:
    print("normal")
elif 25<=bmi<=29.9:
    print("overweight")
else:
    print("obese")

    
#4.
units=int(input("enter units"))
charge=0
if 0<units<100:
    charge=units*1
elif 100<units<200:
    charge=100+(units-100)*2
else:
    charge=300+(units-200)*3
print(charge)

#5
num=input()
res=0
l=len(num)
for i in num:
    res += int(i)**l
if res == int(num):
    print("Amstrong number")
else:
    print("Not a Amstrong")
    '''
#6

'''   
#7
balance=int(input())
if balance>=500 and balance % 100==0:
    print("success")
else:
    print("Insufficient Balance")


#8  
age=int(input("enter the age"))
price=200
fare=0
if age<5:
    fare=0
elif 5<age<18:
    fare=price-price*0.5
elif age>=60:
    fare=price-price*0.3
else:
    fare=price
print(fare)


#11
marks=int(input())
if 90 <= marks <= 100:
    print("A")
elif 85 <= marks <= 89:
    print("B+")
elif 80 <= marks <= 84:
    print("B")
elif 70 <= marks <= 79:
    print("C")
else:
    print("F")
    
#13
day=input()
age=int(input())
if day=="saturday" or day=="sunday":
    price=200
else:
    price=150
    if age<12:
        price=200*0.5
print(int(price))
  

#14
angle=int(input())
if 0<angle<90:
    print("Acute")
elif angle == 90:
    print("Right")
elif 90< angle<180:
    print("Obtuse")
elif angle==180:
    print("Straight")
else:
    print("Reflex")
    
#15
a=int(input())
b=int(input())
c=int(input())
avg=(a+b+c)/3
if avg>90 and a>70 and b>70 and c>70:
    print("Admit")
elif avg>80:
    print("Waitlist")
else:
    print("Reject")

#17
a,b,c=map(int,input().split(","))
if a<90 and b<90 and c<90:
    print("Acute")
elif a==90 and b==90 and c==90:
    print("Right angle")
elif a>90 and b>90 and c>90:
    print("obtuse")
else:
    print("Invalid")

#18
marks=int(input())
if 91<=marks<=100:
    print(10)
elif 81<=marks<=90:
    print(9)
elif 71<=marks<=80:
    print(8)
elif 61<=marks<=70:
    print(7)
elif 51<=marks<=60:
    print(6)
elif 41<=marks<=50:
    print(5)
elif 31<=marks<=40:
    print(4)
elif 21<=marks<=30:
    print(3)
elif 11<=marks<=20:
    print(2)
elif 1<=marks<=10:
    print(1)
else:
    print(0)
#19
num=input()
n1=int(num[0])
n2=int(num[1])
n3=int(num[2])
n4=int(num[3])
s1=n1+n2
s2=n3+n4
if s1==s2:
    print("Lucky")

else:
    print("Not Lucky")
#or
num=input()
if len(num) % 2 == 0:
    l=list(map(int,num))
    if sum(l[:n//2])==sum(l[:n//2]):
        print("lucky num")
else:
    print("Unlucky num")
    
#20  
age=int(input())
experience=int(input())
if age<25 and experience<3:
    print("High risk")
else:
    print("Low risk")
#24 
temp=int(input())
if temp<10:
    print("Very Cold")
elif 10<=temp<=20:
    print("Cold")
elif 21<=temp<=30:
    print("Warm")
else:
    print("Hot")
'''    '''
#30
num=input("enter the number")
if len(num) == 10:
    if num.isdigit():
        s="6789"
        if num[0] in s:
            print("valid number")
        else:
            print("Number needs to start with 6-9")
    else:
        print("enter the digits properly [0-9]")
else:
    print("length needs to 10")
#29
a,b,c=tuple(map(int,input().split()))
if a<=b and b<=c:
    print("Improving")
elif a>=b and b>=c:
    print("Decreasing")
else:
    print("fluctuating")
    
#28
attendance=int(input())
if attendance >=75:
    print("write the exam")
else:
    print("dont allow")

#27
data={
    1:"mon - wd",
    2:"Tue - wd",
    3:"wed - wd",
    4:"Thur - wd",
    5:"fri - wd",
    6:"sat - we",
    7:"sun - we",
    }
num=int(input())
print(data[num])

#26
num=input()
if len(set(num))==len(num):
    print("unique")
else:
    print("duplicates")
print(len(num)-len(set(num)))

#25
plan=float(input())
if plan<1:
    print("Plan A")
elif plan <5:
    print("Plan B")
else:
    print("Plan C")
    
#24
temp=int(input())
if temp<10:
    print("Very cold")
elif 10<=temp<=20:
    print("Cold")
elif 21<=temp<=30:
    print("warm")
else:
    print("Hot")
    
#23
hrs,min=tuple(map(int,input("enter the time (HH:MM):").split(":")))
if 0<=hrs<24 and 0<=min<60:
    print("valid")
else:
    print("invalid")

#22
digit=input()
if len(digit)==1:
    print("Single Digit")
elif len(digit)==2:
    print("Double Digit")
elif len(digit)==3:
    print("Triple Digit")
else:
    print(f"{len(digit)}")
    
#21
age=int(input())
if age<12:
    print("50")
elif 12<=age<60:
    print("100")
else:
    print("60")
#9
hrs,mins=tuple(map(int,input().split(':')))
if 12<=hrs<=23:
    print(f"{hrs-12}:{mins} PM")
elif 0<=hrs<12:
    print(f"{hrs}:{mins} AM")
    '''
'''
65 -90-capital alphabets
97-122-small letters
48-57-num
#12
amount=int(input())
while amount>=10:
    if amount>2000:
        freq=amount//2000
        amount=amount % 2000
        print(f"{freq}*2000")
    elif amount>500:
        freq=amount//500
        amount=amount % 500
        print(f"{freq}*500")
    elif amount>100:
        freq=amount//100
        amount=amount % 100
        print(f"{freq}*100")
    elif amount>50:
        freq=amount//50
        amount=amount % 50
        print(f"{freq}*50")
    elif amount>10:
        freq=amount//10
        amount=amount % 10
        print(f"{freq}*10")
#or

amount=int(input())
curr=[2000,500,100,50,10]
for i in curr: 
    if amount>i:
        freq=amount//i
        amount=amount % i
        print(f"{freq}*{i}")
#16
num=int(input())
sum_of_div=0
for i in range(1,num//2+1):
    if num%i==0:
        sum_of_div+=i
        print(i,end=" ")
if sum_of_div==num:
    print("perfect number")
else:
    print("not a perfect number.Because the sum is",sum_of_div)
    
'''
