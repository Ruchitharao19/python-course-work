'''
syntax:
def func_name():
    #statements
func_name()

def wish(name):
    print(f" welcome to the class {name}")
wish("ruchitha")
wish("varsha")

#positional Arguments
def display(username, mail, pwd):
    print(f" username :{username} \nmail:{mail} \npwd:{pwd}")
uname=input("username:")
mail=input("mail:")
pwd=input("pwd:")
display(username=uname, mail, pwd)

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