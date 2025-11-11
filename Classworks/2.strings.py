'''
string operations

'''
#String Concatenation-Joining 2 or more strings

s1='Ruchitha'
s2='Rao'
print("s1 + s2:",s1 + s2)
print("s1 +' '+ s2:",s1 +' '+ s2)

#String Repetition-Repeating a string multiple times

print("s1 * 10:",s1 * 10)
print('*'*10)
print('r'*10)

#Indexing-Accessing individual characters using indices
'''
R  u  c  h  i  t  h  a
0  1  2  3  4  5  6  7 -Positive Indexing
-8-7 -6 -5 -4 -3 -2 -1 -Negative Indexing
'''
print("s1[3]:",s1[3]) #output-s1[3]:h(4th character)
print("s1[-1]:",s1[-1]) #output-s1[-1]:a(last character)

#slicing-Extracting a part of the string
names="RuchithaNeelimaKavitha"
#syntax=string_name[start : end+1 : step]

print("names[0:8:1]:",names[0:8:1])#names[0:8:1]: Ruchitha
print("names[8:15:1]:",names[8:15:1])#names[8:15:1]: Neelima
print("names[15:22:1]:",names[15:22:1])#names[15:22:1]: Kavitha
print("names[15::1]:",names[15::1])#names[15::1]: Kavitha
print("names[-7::1]:",names[-7::1])#names[-7::1]: Kavitha
print("names[-14:-7:1]:",names[-14:-7:1])#names[-14:-7:1]: Neelima
print("names[-14::1]:",names[-14::1])#names[-14::1]: NeelimaKavitha
print("names[:-14:1]:",names[:-14:1])#names[:-14:1]: Ruchitha
print("names[::-1]:",names[::-1])#names[::-1]: ahtivaKamileeNahtihcuR

#membership operation
print('Ruchitha' in names)#True
print('Ruchi' in names)#True
print('Kavitha' in names)#True
print('Neelima' not in names)#False
print('varsha' in names)#False
#Case Conversion Methods
print(names.upper())#Converts all characters to uppercase.
print(names.lower())#Converts all characters to lowercase.
print(names.title())#Capitalizes the first character.
print(names.capitalize())#Capitalizes the first letter of each word.
print(names.swapcase())#Swaps case: upper → lower, lower -> upper.
print(names.casefold())#Converts to lowercase (more aggressive than lower()).
#Alignment & Formatting Methods
print(s1.center(100,'*'))#Centers the string within width.
print(s1.center(100,'-'))
print(s1.ljust(100,'*'))#Left-aligns the string within width.
print(s1.rjust(100,'*'))#Right-aligns the string within width.
print(s1.zfill(10))#Pads the string with zeros on the left.
print(s1.format())#formats strings dynamically.
n="Ruchitharao"
#Search & Find Methods
print(n.find('u'))#Returns the index of first occurrence, -1 if not found.
print(n.find('R'))
print(n.rfind('a'))#Returns the last occurrence of the substring.
print(n.count('u'))#Counts how many times sub appears.
print(n.index('h'))#Like find(), but raises an error if not found.
print(n.rindex('r'))#Like rfind(), but raises an error if not found.
#Replace & Modify Methods
print(n.replace('h','*'))#Replaces occurrences of old with new.
print(n.replace('a','-'))
print(n.maketrans('hra','***'))#Creates a translation table for translate().
print(n.translate(n.maketrans('hra','***')))#Replaces characters using a translation table.
#Splitting & Joining methods
v="python programing"
print(v.split())#Splits the string into a list by sep.
print(v.split('o'))
v="python,programing,lang"
print(v.split(','))
print(v.rsplit(',',1))#Splits from the right side.
print(v.splitlines())
print(v.join("-"))
print(v.partition("."))
print(v.rpartition("-"))
#Whitespace & Trimming Methods
print(v.strip())#To remove white spaces
print(v.rstrip())#To remove rightside white spaces
print(v.lstrip())#To remove leftside white spaces
#Encoding & Decoding Methods
'''
encode-converting string into bytes
devode-converting bytes into string
'''
u='hello'
#String Testing Methods
print(u.startswith('h'))#True
print(u.endswith('o'))#True
print(u.isalpha())#True
print(u.isalnum())#True
print(u.islower())#True
print(u.isupper())#False
print(u.isspace())#False
print(u.istitle())#False
print(u.isidentifier())#True
#len() - Returns the length of the string.
print(len(u))#5
#max() - Returns the maximum
print(max(u))#o
#min() - Returns the minimum
print(min(u))#e
#sorted() - Returns a sorted list of characters.
print(sorted(u))#['e', 'h', 'l', 'l', 'o']
#chr() / ord() - Converts between characters and their ASCII codes.
print(chr(97))#a
print(ord("a"))#97
print('123'.isdecimal())#True
print('123'.isdigit())#True
print('12.3'.isdigit())#True
print('abc'.isnumeric())#False