'''
output formating
'''
#printing text
print("ruchitha rao")
#Printing Multiple Items
name = "Raghav"
age = 24
print("Name:", name, "Age:", age)
#-Using sep to Change the Separator
print("2003","12","19",sep="-")
print("Ruchitha", end=" ")
print("Raghav")
print("Raghav \nRuchitha")
print("Name:\t",name)
#1-using Commas
name = "Raghav"
age = 24
score=9.8
print("name:",name,"\tage:",age,"\tscore:",score,sep="")
#2-using Modulo Operator (% Formatting)
score=9.8888888
print("name: %s age: %d score: %.2f" %(name,age,score))
#3-Using f-strings (Formatted String Literals)
print(f"name:{name} age:{age} score:{score:.2f}")
#4-Using str.format() Method
print("name:{} age:{} score:{:.3f}".format(name,age,score))
