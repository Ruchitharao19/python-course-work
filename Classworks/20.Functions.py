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

def shoot(bullets):
    if bullets<=0:
        print("game over")
        return
    print(f"{bullets} bullets left")
    shoot(bullets-1)
shoot(10)
'''
def display(n,i):
    if i>len(n):
        print("Exit")
        return
    print(n[i])
    display(n+1)
display(n)
'''