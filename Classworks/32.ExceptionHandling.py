try:
    a=10/0
except ZeroDivisionError:
    print("you can't divide a number with zero")
else:
    print("you have divided successfully")
finally:
    print("end of the try block")
print("rest of the code")
print("--------------------")

try:
    a=int([1,2,3])
except ZeroDivisionError:
    print("you can't divide a number with zero")
except NameError:
    print("you didnot define the variable")
except TypeError:
    print("you can change this data type into other one")
else:
    print("you have divided successfully")
finally:
    print("end of the try block")
print("rest of the code")

print("--------------------")

try:
    a=int([1,2,3])
except (ZeroDivisionError,NameError,TypeError,KeyError,IndexError) as e :
    print("error occured:",e)

    print("you can change this data type into other one")
else:
    print("you have divided successfully")
finally:
    print("end of the try block")
print("rest of the code")
print("--------------------")


try:
    a=a+[1,2,3]
except Exception as e :
    print("error occured:",e)

    print("you can change this data type into other one")
else:
    print("you have divided successfully")
finally:
    print("end of the try block")
print("rest of the code")
print("--------------------")

try:
    a=int(input("enter the number:"))
    if a<0:
        raise Exception("Negative number  not allowed")
except Exception as e :
    print("error occured:",e)

    print("you can change this data type into other one")
else:
    print("you have divided successfully")
finally:
    print("end of the try block")
print("rest of the code")
print("--------------------")

try:
    a=int(input("enter the number:"))
    try:
        a=b/10
    except Exception as e :
        print("error occured:",e)

except Exception as e :
    print("error occured:",e)

    print("you can change this data type into other one")
else:
    print("you have divided successfully")
finally:
    print("end of the try block")
print("rest of the code")
