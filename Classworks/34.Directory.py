#To create a folder
import os
os.mkdir("Batch-41")

#To remove a folder
import os
os.rmdir("Batch-41")

#Removing a Non-Empty Directory
import os
import shutil
shutil.rmtree("Batch-41")

#Creating Nested Directories
import os
os.makedirs("Batch-41/demo")

#Listing Files in a Directory
import os
res=os.listdir()
print(res)
import os
print(os.getcwd())

#Checking if a Directory Exists
import os
os.mkdir('python programming')#To create a folder
path=os.path.join('python programming','demo.txt')#Join File Path
print(os.path.exists(path))
with open(path,"w") as file:
    file.write("hello")
    
#Changing the Current Working Directory   
import os
print(os.getcwd())
os.chdir("mails")
