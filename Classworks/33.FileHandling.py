try:
    file=open("names.txt",'r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.read())
    file.close()

try:
    file=open("names.txt",'r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.readline())
    file.close()

try:
    file=open("names.txt",'r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.readlines())
    file.close()

try:
    file=open("names.txt",'r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()

try:
    with open("names.txt",'r') as file:
        print(file.read())
        file.seek(0)
        print(file.readline())
        file.seek(0)
        print(file.readlines())
except FileNotFoundError:
    print("File is not present")

#write mode
with open("names.txt",'w') as file:
    file.write("File operations")
#append mode
with open("names.txt",'a') as file:
    file.write("1.exception")

with open("names.txt",'r+') as file:
    file.write("1.exception")
    file.seek(0)
    print(file.read())
with open("names.txt",'w+') as file:
    file.write("1.exception")
    file.seek(0)
    print(file.read())  
