'''
syntax:
c=[res for i in seq]
'''
#list comprehension
#1 to 10 numbers
l=[]
for i in range(1,11):
    l.append(i)
print(l)
l=[i for i in range(1,11)]
print(l)
#multiles of 2
l=[]
for i in range(2,51,2):
    l.append(i)
print(l)
l=[i for i in range(2,51,2)]
print(l)
#square of a number
l=[]
for i in range(1,11):
    i=i**2
    l.append(i)
print(l)
l=[i**2 for i in range(1,11)]
print(l)

vol="aeiouAEIOU"
sen=input("enter the sen:")
res=[]
for i in sen:
    if i in vol:
        res.append(i)
print (res)
r=[res for i in sen if i in vol]
print(r)
vol="aeiouAEIOU"
sen=input("enter the sen:")
res=[]
for i in range(5):
    if i in range(5):
        res.append("*")
print (res)
r=["*" for i in range(5) if i in range(5)]
print(r)
#tuple comprehension
t=tuple(i for i in range(1,11))
print(t)
#set comprehension
s={i for i in range(1,11)}
print(s)
#dictionary comprehension
d={i:i for i in range(1,11)}
print(d)

d={i:i*i for i in range(1,11)}
print(d)
