'''
Q1. Automated Salary Tax Calculator
A company deducts tax based on the following salary brackets:
● Up to 2,50,000 → No Tax
● 2,50,001 – 5,00,000 → 5%
● 5,00,001 – 10,00,000 → 20%
● Above 10,00,000 → 30%
Write a script that takes annual salary as input and calculates total tax amount.
Input Format
A single float salary
Output Format
Tax amount as float
'''
sal = int(input("Enter the sal: "))
tax=0

if sal<=250000:
    tax=0
elif 250000<sal<=500000:
    tax=sal*0.05
elif 500000<sal<=1000000:
    tax=sal*0.2
elif sal>1000000:
    tax=sal*0.3

print(f'Tax amount: {tax}\nSalary after tax: {sal-tax}')

'''
Q2. Movie Ticket Pricing System
A theater charges differently based on age:
● Below 5: Free
● 5–18: ₹100
● 19–60: ₹150
● Above 60: ₹120

Take the age of n visitors and calculate the total collection.
Input Format
● First line: Integer n
● Next n lines: one age per line

Output Format
Total ticket collection
'''
n=int(input("No of persons: "))
cost=0
for i in range(n):
    age=int(input("Enter the age: "))
    if age<5:
        continue
    elif 5<=age<=18:
        cost+=100
    elif 19<=age<=60:
        cost+=150
    elif age>60:
        cost+=120

print(cost)
'''
Q3. Electricity Bill Generator
Design a bill generator based on units consumed:
● First 100 units: ₹1.5/unit
● 101–200 units: ₹2.5/unit
● 201–500 units: ₹4/unit
● Above 500 units: ₹6/unit

Input Format
Integer units
Output Format
Total bill in rupees
'''
units=int(input("Enter the units: "))
price=0
if units<=100:
    price=units*1.5
elif 100<units<=200:
    price=150+(units-100)*2.5
elif 200<units<=500:
    price=400+(units-200)*4
elif units>500:
    price=1600+(units-500)*6

print(price)

'''
Q4. Car Parking Fee Calculator
Charges are based on hours parked:
● Up to 2 hours → ₹30
● Every additional hour → ₹10/hr
● Max per day (24 hrs) → ₹200

Input Format
Integer hours

Python

Python

Python

Python
Output Format
Fee amount
'''
hrs=int(input("Enter the hours: "))
fee=0
if hrs<=2:
    fee=30
elif 2<hrs<24:
    fee=30+(hrs-2)*10
elif hrs==24:
    fee=200

print(fee)

'''
Q5. Product Inventory Checker (Nested Conditionals)
Take product name and quantity as input. Based on quantity:
● 0 → Out of Stock
● 1–10 → Low Stock
● 11–50 → In Stock
● Above 50 → Overstocked

Input Format
● First line: Product name

Python

Python

Python

Python
● Second line: Integer quantity

Output Format
Message as per condition
'''

name=input("Enter the name: ")
qua=int(input("Enter the qua: "))
if qua==0:
    print(f'{name}: Out of Stock')
elif 0<qua<=10:
    print(f'{name}: Low Stock')
elif 10<qua<=50:
    print(f'{name}:  In Stock')
elif qua>50:
    print(f'{name}:  Overstocked')
'''
Q6. Pattern – Row-wise Alternating 0 and 1 (Nested Loops)
Write a program to print a square pattern of size n, where each row alternates between 0
and 1.
Input Format
An integer n
Output Format
Pattern as described
'''

n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=' ')
    print()
'''
Q7. Gym Subscription Billing (Menu Driven Program)
Menu:
1. Monthly – ₹500
2. Quarterly – ₹1300
3. Yearly – ₹5000
Write a menu-driven script to calculate bill amount based on user choice and number of
persons.
Input Format
● Line 1: Choice (1/2/3)
● Line 2: Number of people
Output Format
Total bill amount
'''

billing={1:500,2:1300,3:5000}
ch=int(input("Enter the choice: "))
n=int(input("No of ppl: "))

print(billing[ch]*n)

'''
Q8. Billing Bot – Apply Discount Based on Amount
You are creating a billing bot. Apply discount based on total purchase:
● ₹0–999 → No discount
● ₹1000–4999 → 5%
● ₹5000–9999 → 10%

Python

Python

Python
● ₹10000+ → 15%

Input Format
A float value representing total amount
Output Format
Final payable amount after discount
'''
amount=float(input("Enter the amount: "))
discount=0
if 0<=amount<1000:
    discount=0
elif 1000<=amount<5000:
    discount=amount*0.05
elif 5000<=amount<10000:
    discount=amount*0.1
elif amount>10000:
    discount=amount*0.15

print(amount-discount)
'''
Q9 : ATM PIN Verification with Blocking Logic
Create a script for an ATM system where a user gets 3 chances to enter the correct 4-digit
PIN.
● If the correct PIN is entered, display "Access Granted".
● If all 3 attempts are wrong, print "ATM Blocked. Try Again Later."

Stored PIN: 1234
Input Format
Three lines: each a 4-digit integer PIN attempt
Output Format
Result message based on attempts
'''


str_pin=1234
for i in range(3):
    pin=int(input("Enter the pin: "))
    if pin==str_pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked. Try Again Later.")

'''
Q10 : Bus Booking System – Track Full and Empty Seats
A bus has n seats. You are given a list of seat numbers booked (1 to n).
● Print total seats
● Count and print number of booked seats and available seats

Input Format
● Line 1: Integer n – total number of seats
● Line 2: Space-separated list of booked seat numbers

Output Format

Python

Python

Python

Python
● Total seats
● Booked seats count
● Available seats count
'''
n=int(input("Enter the no of seats: "))
bs= tuple(map(int,input().split()))

print(f'Total Seats: {n}\nBooked: {len(bs)}\nAvailable: {n-len(bs)}')
