'''
Q1. Compute Geometric Values (Math Module)
You're designing a calculator for engineers. Use the math module to write a function
circle_geometry(radius) that returns:
● The area of the circle (πr2)
● The circumference (2πr)
Round both values to 2 decimal places and return as a tuple.
Test Cases:
● circle_geometry(7) → (153.94, 43.98)
● circle_geometry(2.5) → (19.63, 15.71)
'''
import math
def circle_geometry(r):
    t=(round(math.pi*r*r,2), round(2*math.pi*r,2))
    print(t)
circle_geometry(7)
circle_geometry(2.5)
'''
Q2. Random Team Picker (Random Module)
Write a function pick_random_team(members, team_size) that randomly selects
team_size unique names from the members list using the random module.
Test Cases:
● pick_random_team(["Alice", "Bob", "Charlie", "David"], 2) → Any 2 random names
● pick_random_team(["A", "B", "C", "D", "E"], 3) → Any 3 random names
'''
import random
def pick_random_team(members, team_size):
    print(random.choices(members,k=team_size))
pick_random_team(["Alice", "Bob", "Charlie", "David"], 2)
pick_random_team(["A", "B", "C", "D", "E"], 3)
'''
Q3. Temperature Alert (Lambda + Filter)
You are given a list of temperature readings.
Write a lambda expression with filter() to select all temperatures above 40°C.
Test Cases:
● input: [36, 42, 39, 45, 41] → [42, 45, 41]
● input: [30, 32, 38] → []
'''
temp=[36, 42, 39, 45, 41]
res=list(filter(lambda i:i>40,temp))
print(res)
'''
Q4. Identify Prime Numbers (Recursion)
Write a recursive function is_prime(n, i=2) that returns True if n is a prime number.
No loops or built-in prime functions allowed.
Test Cases:
● is_prime(11) → True
● is_prime(15) → False
'''
def is_prime(n):
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c+=1
            break
    if c==0:
        return True
    else:
        return False
    
n=int(input("Enter the number: "))
print(is_prime(n))
    
    
'''
Q5. Reverse Digits (Recursion)
Write a recursive function reverse_number(n) that returns the reverse of a number.
Test Cases:
● reverse_number(1234) → 4321
● reverse_number(450) → 54
'''
def reverse_number(n):
    if n<=0:
        return
    print(n%10,end='')
    return reverse_number(n//10)
reverse_number(1234)
reverse_number(450)  

'''
Q6. Filter by Starting Letter (Lambda)
Given a list of strings, write a function using filter() and lambda to return only the
strings that start with a given character.
Test Cases:
● input: (["cat", "car", "bat", "apple"], 'c') → ['cat', 'car']
● input: (["apple", "banana", "apricot"], 'a') → ['apple', 'apricot']
'''
inp=["cat", "car", "bat", "apple"]
ch='c'
res=list(filter(lambda i: i.startswith(ch),inp))
print(res)
'''
Q7. Create Your Own Utility Module (User-Defined Module)
Create a user-defined module named string_utils.py that includes:
● A function is_palindrome(word) → returns True if the word is a palindrome
● A function capitalize_words(text) → returns text with each word capitalized
Then write a main program to import and use both functions.
Test Cases:
●  is_palindrome("madam")→ True
● capitalize_words("hello world") → "Hello World"
'''
#string_utils.py
def is_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
def capitalize_words(text):
    return text.capitalize()
#main.py
#from string_utils import is_palindrome,capitalize_words
print(is_palindrome("madam"))
print(capitalize_words("hello world"))
    
'''
Q8. Remove Duplicates Case-Insensitive (Set + Lambda)
Write a function remove_duplicates(words) that removes duplicates from a list
case-insensitively and returns lowercase unique words.
Test Cases:
● ["Apple", "apple", "Banana", "BANANA", "Cherry"] → ['apple', 'banana', 'cherry']
'''
words=["Apple", "apple", "Banana", "BANANA", "Cherry"]
res=set(map(lambda i : i.lower(),words))
print(res)
'''
Q9. Countdown Timer (Generator)
Write a generator function countdown(n) that yields numbers from n to 0 (inclusive), one
at a time.
Test Cases:
● countdown(3) → yields: 3, 2, 1, 0
● countdown(5) → yields: 5, 4, 3, 2, 1, 0
'''
def countdown(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
c=countdown(n)
for i in range(n+1):
    print(next(c))

'''
Q10. Nested Sum (Recursion)
Write a function nested_sum(lst) that computes the sum of all numbers in a list, which
may contain other nested lists.
Test Cases:
● nested_sum([1, [2, 3], 4]) → 10
● nested_sum([[1, 2], [3, [4, 5]]]) → 15
'''
def nested_sum(lst):
    for i in lst:
        if type(i)=="class 'list'>":
            nested_sum(i)
        else:
            print(i)
nested_sum([1, [2, 3], 4])
