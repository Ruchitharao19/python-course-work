
#form validiation
import re

name=input("Enter the name: ")
pattern=r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res=bool(re.fullmatch(pattern,name))
print(res)

email=input("Enter the email: ")
pattern=r'^[A-Za-z0-9.-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$'
res=bool(re.fullmatch(pattern,email))
print(res)


phno=input("Enter the phno: ")
pattern=r'^(?:\+91|0)?{[6-9]\d{9}$'
res=bool(re.fullmatch(pattern,phno))
print(res)


username=input("Enter the username: ")
pattern=r'^[a-zA-Z0-9]{5,15}$'
res=bool(re.fullmatch(pattern,username))
print(res)

phno=input("Enter the phno: ")
pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%?&]{8,}$'
res=bool(re.fullmatch(pattern,phno))
print(res)
