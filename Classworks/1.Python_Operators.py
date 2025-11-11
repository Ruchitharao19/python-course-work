'''
Python Operators
----------------
'''
#1.arthametic Operators
a=40
b=60
print("a+b:",a+b) #a+b: 100
print("a-b:",a-b) #a-b: -20
print("a*b:",a*b) #a*b: 2400
print("a/b:",a/b) #a/b: 0.6666666666666666
print("a//b:",a//b) #a//b: 0
print("a**b:",a**b) #a**b: 1329227995784915872903807060280344576000000000000000000000000000000000000000000000000000000000000

#2.Comparison Operators
c=20
d=40
print("c<d:",c<d) #c<d: True
print("c>d:",c>d) #c>d: False
print("c<=d:",c<=d) #c<=d: True
print("c>=d:",c>=d) #c>=d: False
print("c==d:",c==d) #c==d: False
print("c!=d:",c!=d) #c!=d: False

#3.Assignment operators
'''
var = var op val
var op = val
'''
e=100
e+=100
print("e+=100:",e) #e+=100:200
e-=100
print("e-=100:",e) #e-=100:100
e*=100
print("e*=100:",e) #e*=100:10000
e/=100
print("e/=100:",e) #e/=100:100.0
e//=100
print("e//=100:",e) #e//=100:1.0
e**=10
print("e**=100:",e) #e**=100:1.0

#4.Logical Operators
'''
Logical and

T and T= T
T and F= F
F and T= F
F and F= F

'''
r=100
p=50
print("r%20==0 and p%20==0:",r%20==0 and p%20==0) #r%20==0 and p%20==0:False
'''
Logical or

T or T= T
T or F= T
F or T= T
F or F= F

'''
print("r%20==0 or p%20==0:",r%20==0 or p%20==0) #r%20==0 or p%20==0:True
'''
Logical NOT

not T= F
not F= T

'''
print("not r%20==0:", not r%20==0 ) #not r%20==0:False
print("not p%20==0:", not p%20==0 ) #not p%20==0:True

#5.Membership Operators
s='python'
print("'i' in s:",'i' in s)#'i' in s: False
print("'i' not in s:",'i' not in s)#'i' not in s: True
l=[1,2,3,4,5]
print("'3' in l",3 in l)#'3' in l True
print("'10' not in l",10 not in l)#'10' not in l True
t=(10,20,30,40)
print("'10' in t",10 in t)#'10' in t True
print("'50' not in t",50 not in t)#'50' not in t True
s={22,33,44,55}
print("'22' in s",22 in s)#'22' in s True
print("'66' not in s",66 not in s)#'66' not in s True
d={1:10,2:20,3:30}
print("'2' in d",2 in d)#'2' in d True
print("'22' not in d",22 not in d)#'22' not in d True

#6.Identity operations
a=[1,2,3,4]
b=[1,2,3,4]
print("a is b:",a is b)#a is b: False
c=a
print("a is c:",a is c)#a is c: True
print("id(a):",id(a))#id(a): 1667843404608
print("id(b):",id(b))#id(b): 1667843519552
print("id(c):",id(c))#id(c): 1667843404608
print("a is not b:",a is not b)#a is not b: True
print("a is not c:",a is not c)#a is not c: False
x="ruchi"
y="ruchi"
print("x is y:",x is y)
z=x
print("x is z:",x is z)
print("id(x):",id(x))
print("id(z):",id(z))
#7.Bitwise Operations
'''
1-0001
2-0010
3-0011
4-0100
5-0101
6-0110
7-0111
8-1000
9-1001
10-1010
'''
'''
&-and gate
00=0
10=0
01=0
11=1

4-0100
5-0101
-------
  0100
-------
'''
print("4&5:",4&5)#4
'''
|-or gate
00=0
10=1
01=1
11=1

11-1011
12-1100
-------
   1111
-------
'''
print("11|12:",11|12)#15
'''
^ xor gate
00=0
01=1
10=1
11=0

9- 1001
10-1010
-------
   0011
-------
'''
print("9^10:",9^10)#3

'''
~ not gate
0=1
1=0
'''
print("~16:",~16)
#<<-left shift
print("22<<1:",22<<1)#44
#>>-right shift
print("26>>2:",26>>2)#6