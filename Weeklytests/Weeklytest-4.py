'''
Q1. Calculate BMI
Write a function calculate_bmi(weight_kg, height_m) that returns the Body Mass
Index (BMI), rounded to two decimal places.
Formula: BMI = weight / (height * height)

Test Cases:
calculate_bmi(70, 1.75) → 22.86
calculate_bmi(90, 1.8) → 27.78
'''
def calculate_bmi(weight_kg, height_m):
    BMI=weight_kg / (height_m * height_m)
    print(round(BMI,2))
    print('%.2f'%(weight_kg / (height_m * height_m)))

calculate_bmi(70, 1.75)
calculate_bmi(90, 1.8)
'''
Q2. Filter Even Numbers
Write a function filter_even(numbers) that takes a list of integers and returns a new list
containing only the even numbers.

Test Cases:
filter_even([1, 2, 3, 4, 5, 6]) → [2, 4, 6]
filter_even([11, 15, 21]) → []
'''
def  filter_even(numbers):
    res=[i for i in numbers if i%2==0]
    print(res)

filter_even([1, 2, 3, 4, 5, 6])
filter_even([11, 15, 21])
'''
Q3. Generate Multiplication Table
Create a function generate_table(n) that returns the multiplication table of a number n
from 1 to 10 in a list format.

Test Cases:
generate_table(2) → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
generate_table(5) → [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
'''
def generate_table(n):
    table=[i*n for i in range(1,11)]
    print(table)

generate_table(2)
generate_table(5)
'''
Q4. Check Anagram
Write a function is_anagram(str1, str2) that returns True if both strings are
anagrams of each other, ignoring case and spaces.

Test Cases:
is_anagram("listen", "silent") → True
is_anagram("Hello", "Olelh") → True
is_anagram("apple", "pale") → False
'''
def is_anagram(str1, str2):
    if sorted(str1.lower())==sorted(str2.lower()):
        return True
    else:
        return False

print(is_anagram("listen", "silent"))
print(is_anagram("Hello", "Olelh"))
print(is_anagram("apple", "pale"))
'''
Q5. Count Word Occurrences
Write a function count_words(text) that takes a sentence and returns a dictionary
mapping each word to its frequency.

Test Cases:
count_words("this is a test this is") → {'this': 2, 'is': 2,
'a': 1, 'test': 1}
count_words("hello hello world") → {'hello': 2, 'world': 1}
'''
def count_words(text):
    res={}
    for i in text.split():
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    print(res)


count_words("this is a test this is")
count_words("hello hello world")
'''
Q6. Simulate LRU Cache
Write a function lru_cache(requests, size) that simulates a Least Recently Used
(LRU) Cache. Return the final state of the cache as a list.
● When an item is requested:
○ If already in cache: move it to the front (most recently used).
○ If not in cache:
■ If space available: add to front.
■ If full: remove last item, then add new item to front.

Test Cases:
lru_cache([1,2,3,2,4,1], 3) → [1, 4, 2]
lru_cache([5,6,7,8], 2) → [8, 7]
lru_cache([1,2,3,1], 2) → [1, 3]
'''
def lru_cache(requests, size):
    cache=[]
    for i in requests:
        if i in cache:
            cache.remove(i)
            cache.insert(0,i)
        else:
            if len(cache)<size:
                cache.insert(0,i)
            else:
                cache.pop()
                cache.insert(0,i)

    print(cache)

lru_cache([1,2,3,2,4,1], 3)
lru_cache([5,6,7,8], 2)
lru_cache([1,2,3,1], 2)
'''
Q7. Flatten 2D List
Write a function flatten_matrix(matrix) that takes a 2D list and returns a flattened
version of the list in row-major order.

Test Cases:
flatten_matrix([[1, 2], [3, 4]]) → [1, 2, 3, 4]
flatten_matrix([[5], [6, 7], [8]]) → [5, 6, 7, 8]
'''
def flatten_matrix(matrix):
    res=[]
    for i in matrix:
        for j in i:
            res.append(j)
    print(res)
flatten_matrix([[1, 2], [3, 4]])
flatten_matrix([[5], [6, 7], [8]])
'''
Q8. Create Email Address
Write a function create_email(first_name, last_name, domain) that returns an
email in the format:
firstname.lastname@domain.com
All values should be converted to lowercase.
Test Cases:

create_email("John", "Doe", "gmail") → "john.doe@gmail.com"
create_email("ALICE", "Smith", "yahoo") →
"alice.smith@yahoo.com"
'''
def create_email(first_name, last_name, domain):
    print(f'{first_name.lower()}.{last_name.lower()}@{domain.lower()}.com')
create_email("John", "Doe", "gmail")
create_email("ALICE", "Smith", "yahoo")
'''
Q9. Find All Factors of a Number
Write a function get_factors(n) that returns a list of all positive factors of n in
ascending order.

Test Cases:
get_factors(12) → [1, 2, 3, 4, 6, 12]
get_factors(17) → [1, 17]
get_factors(28) → [1, 2, 4, 7, 14, 28]
'''
def get_factors(n):
    res=[]
    for i in range(1,n//2+1):
        if n%i==0:
            res.append(i)
    res.append(n)
    print(res)
get_factors(12)
get_factors(17)
get_factors(28)
'''
Q10. Format Invoice Entry
Write a function format_invoice(item, quantity, price) that returns a string in the
format:
"{item} x{quantity} @ ₹{price} = ₹{total}"
Where total = quantity × price

Test Cases:
format_invoice("Pen", 3, 10) → "Pen x3 @ ₹10 = ₹30"
format_invoice("Notebook", 2, 45) → "Notebook x2 @ ₹45 = ₹90"
'''
def format_invoice(item, quantity, price):
    total = quantity * price
    print(f'{item} x{quantity} @ ₹{price} = ₹{total}')

format_invoice("Pen", 3, 10)
format_invoice("Notebook", 2, 45)
