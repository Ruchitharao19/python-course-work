'''
syntax:
def func_name():
    #statements
func_name()
'''
def wish(name):
    print(f" welcome to the class {name}")
wish("ruchitha")
wish("varsha")

#positional Arguments:Arguments are passed in the order they are defined in the function.
def display(username, mail, pwd):
    print(f" username :{username} \nmail:{mail} \npwd:{pwd}")
uname=input("username:")
mail=input("mail:")
pwd=input("pwd:")
display(uname, mail, pwd)
display(mail, uname, pwd)
#Keyword Arguments:Arguments are specified with the parameter names.
def display(username, mail, pwd=123):
    print(f" username :{username} \nmail:{mail} \npwd:{pwd}")
uname=input("username:")
mail=input("mail:")
pwd=input("pwd:")
display(uname, mail)
#Default Arguments:Provides default values if no argument is provided.
def add(*num):
    return sum(num)
print(add(1,2,3))
'''
Variable-Length Arguments *args
1:(Arbitrary Positional ArgumentsUsed to pass a variable number of arguments.
2:**kwargs (Arbitrary Keyword Arguments)Used to pass multiple keyword arguments.
'''
def display(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
display(name="Alice", age=25, city="New York")
#local scope
def display():
    mess="hi"
    print(mess)
display()

#Global scope
x=10
def show():
    x=20
    print("inside:",x)
show()
print("outside:",x)

x = 10
def update():
    global x
    x = 20
    print("inside:",x)
update()
print("outside:",x)
#Enclosing Scope
def outer():
    msg = "Hi"
    def inner():
        print("inside:",msg)
    inner()
outer()

def outer():
    msg = "Hi"
    def inner():
        nonlocal msg
        msg = "Hello"
    inner()
    print(msg) # Output: Hello
outer()

#recursion
#factorial of a number
def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
#fibonacci series
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))
    
def shoot(bullets):
    if bullets<=0:
        print("game over")
        return
        print(f"{bullets} bullets left")
    shoot(bullets-1)
shoot(10)

#Pass by Value (Immutable Objects)
def modify_value(num):
    num += 10 
    print("Inside function:", num)
x = 5
modify_value(x)
print("Outside function:", x)

#Pass by Reference def modify_value(num):
def modify_list(lst):
    lst.append(4) # Modifies the original list
numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)