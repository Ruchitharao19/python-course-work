#16,12,10,9
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
    
#    
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
    
    
age=int(input())
experience=int(input())
if age<25 and experience<3:
    print("High risk")
else:
    print("Low risk")
    
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
'''
#23
hrs,min=tuple(map(int,input("enter the time (HH:MM):").split(":")))
if 0<=hrs<24 and 0<=min<60:
    print("valid")
else:
    print("invalid")
