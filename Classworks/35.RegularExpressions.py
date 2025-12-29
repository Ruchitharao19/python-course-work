import re
s="python programming"
pattern=r'[0-9A-Za-z]'
res=re.match(pattern,s)
print(res.group() if res else "not found")
#to get first occurance of digit
import re
s="python programming version 13.0"
pattern=r'\d'
res=re.search(pattern,s)
print(res.group() if res else "not found") 
#to get first occurance of  2 digits
import re
s="python programming version 13.0"
pattern=r'\d{2}'
res=re.search(pattern,s)
print(res.group() if res else "not found") 
#to get all the digits in a list
import re
s="python ab33 programming 23 version 13.0"
pattern=r'\d{2}'
res=re.findall(pattern,s)
print(res)
#to find the index
import re
s="python programming version 13.0"
pattern=r'\d{2}'
res=re.finditer(pattern,s)
for i in res:
    print(i.start(),i.group() if i else "not found")
#to split the string based on delimiters
import re
s="python#ab33,programming;23 version 13.0"
pattern=r'[,;#@]'
res=re.split(pattern,s)
print(res)

import re
s="python#ab33,programming;23 version 13.0"
pattern=r'[,;#@]'
res=re.split(pattern,s)
print(res)
#replaces the old string with new string
import re
s="vk18 rh45 do7"
res=re.sub(r'[a-z]','*',s)
print(res)

import re
s="sit cut put"
res=re.findall(r'..t',s)
print(res)

#starts with-^
import re
s="Sit cut put"
res=re.findall(r'^[A-Z]',s)
print(res)

#ends with-$
import re
s="Sit cut put"
res=re.findall(r'[a-z]$',s)
print(res)
#matches 0 or more occurences
import re
s="p py y pyv pyvv pyvvv"
res=re.findall(r'pyv*',s)
print(res)
#atleast one
import re
s="p py y pyv pyvv pyvvv"
res=re.findall(r'pyv+',s)
import re
s="cut put cit ct"
res=re.findall(r'c?t',s)
print(res)

