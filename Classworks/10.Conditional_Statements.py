#conditional statements
'''
if
syntax
if condition:
    statements
'''
num=20
if num>=20:
    print("num is greater than 20")

'''
if else
syntax
if condition:
    statements
else:
    statements
'''
num=int(input("enter value:"))
if num % 2==0:
    print("even")
else:
    print("odd")


'''
if-elif-else
syntax
if condition:
    statements
elif condition:
    statements
else:
    statements
'''
stock = 5 # Limited stock available
if stock > 20:
    print("stock is fully available.")
elif stock > 0:
    print("stock is low, hurry up!")
else:
    print("Sorry, stock not available.")

'''
nestedif
syntax
if condition:
    statements
  if condition:
    statements  
  elif condition:
    statements
  else:
    statements
else:
    statements
'''

stock=int(input("enter value:"))
is_prime_customer = True
if stock > 0:
    print("Amazon stock is available!")
    if is_prime_customer:
        print("Prime customer gets priority shipping!")
    else:
        print("Standard shipping will apply.")
else:
    print("Sorry, Amazon stock is out of stock.")
