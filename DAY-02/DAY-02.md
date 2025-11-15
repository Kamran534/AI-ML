# Day 2: Data Types, Operators & String Manipulation

**Duration:** 3-4 hours | **Date:** 11/14/2025 | **Status:** ⬜ Not Started | ⬜ In Progress | ✅ Completed

---

## 🎯 Today's Goals

By the end of today, you will:
- ✅ Master Python data types (int, float, str, bool)
- ✅ Use arithmetic, comparison, and logical operators
- ✅ Manipulate strings with methods
- ✅ Perform type conversion
- ✅ Get user input and build interactive programs
- ✅ Complete 5+ practical exercises

---

## 📋 Pre-Session Checklist

Before starting:
- [✅] Completed Day 1 successfully
- [✅] Python and VS Code working
- [✅] Can run Python scripts
- [✅] GitHub repository created
- [✅] Review yesterday's code

---

## 🕐 Session 1: Numbers & Arithmetic Operators (45 minutes)

### Part 1.1: Integer and Float Data Types

**Integers (whole numbers):**
```python
# Integers - whole numbers (positive or negative)
age = 25
year = 2024
negative_temp = -15
big_number = 1000000

# You can use underscores for readability
million = 1_000_000
billion = 1_000_000_000

print(age)
print(type(age))  # <class 'int'>
```

**Floats (decimal numbers):**
```python
# Floats - numbers with decimal points
price = 19.99
pi = 3.14159
temperature = 98.6
negative_float = -12.5

# Scientific notation
speed_of_light = 3e8  # 3 × 10^8 = 300000000
tiny_number = 1.5e-3  # 0.0015

print(price)
print(type(price))  # <class 'float'>
```

**Differences between int and float:**
```python
x = 5      # int
y = 5.0    # float

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>

# Division always returns float
result = 10 / 2
print(result)       # 5.0
print(type(result)) # <class 'float'>
```

### Part 1.2: Arithmetic Operators

**Basic Operators:**
```python
# Basic arithmetic operators
a = 10
b = 3

# Addition
addition = a + b
print(f"{a} + {b} = {addition}")  # 10 + 3 = 13

# Subtraction
subtraction = a - b
print(f"{a} - {b} = {subtraction}")  # 10 - 3 = 7

# Multiplication
multiplication = a * b
print(f"{a} * {b} = {multiplication}")  # 10 * 3 = 30

# Division (always returns float)
division = a / b
print(f"{a} / {b} = {division}")  # 10 / 3 = 3.3333...

# Floor Division (rounds down to nearest integer)
floor_div = a // b
print(f"{a} // {b} = {floor_div}")  # 10 // 3 = 3

# Modulus (remainder)
modulus = a % b
print(f"{a} % {b} = {modulus}")  # 10 % 3 = 1

# Exponentiation (power)
power = a ** b
print(f"{a} ** {b} = {power}")  # 10 ** 3 = 1000
```

**Operator Precedence (Order of Operations):**
```python
# PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

result1 = 2 + 3 * 4
print(result1)  # 14 (not 20, because * comes before +)

result2 = (2 + 3) * 4
print(result2)  # 20 (parentheses first)

result3 = 10 + 2 ** 3 * 4
print(result3)  # 42 (exponent first, then multiply, then add)

# Complex expression
result4 = ((10 + 5) * 2) ** 2 / 3 - 8
print(result4)  # 292.0
```

**Shorthand Assignment Operators:**
```python
x = 10

# These two are equivalent:
x = x + 5
x += 5      # Shorthand

# All arithmetic operators have shorthand versions:
x += 5      # x = x + 5
x -= 3      # x = x - 3
x *= 2      # x = x * 2
x /= 4      # x = x / 4
x //= 2     # x = x // 2
x %= 3      # x = x % 3
x **= 2     # x = x ** 2

# Example usage
score = 100
score += 10  # Add 10 points
print(score)  # 110

score *= 2   # Double the score
print(score)  # 220
```

### Part 1.3: Built-in Math Functions

```python
# Built-in functions for numbers
x = -5.7
y = 10

print(abs(x))       # 5.7 (absolute value)
print(round(x))     # -6 (round to nearest integer)
print(round(3.14159, 2))  # 3.14 (round to 2 decimal places)
print(max(5, 10, 3, 8))   # 10 (maximum value)
print(min(5, 10, 3, 8))   # 3 (minimum value)
print(pow(2, 3))    # 8 (2^3, same as 2**3)

# Sum function with list (we'll learn lists later)
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15
```

**Math Module for Advanced Operations:**
```python
import math

# Constants
print(math.pi)     # 3.14159...
print(math.e)      # 2.71828...

# Functions
print(math.sqrt(16))      # 4.0 (square root)
print(math.ceil(3.2))     # 4 (round up)
print(math.floor(3.8))    # 3 (round down)
print(math.factorial(5))  # 120 (5! = 5×4×3×2×1)

# Trigonometry
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
print(math.tan(math.pi/4))  # 1.0

# Logarithms
print(math.log(100, 10))  # 2.0 (log base 10)
print(math.log(8, 2))     # 3.0 (log base 2)
```

### Practice Exercise 1: Temperature Converter

Create `temperature_converter.py`:
```python
# temperature_converter.py - Convert between Celsius and Fahrenheit

print("=== Temperature Converter ===\n")

# Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Fahrenheit to Celsius
fahrenheit = 77
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius}°C")

# Celsius to Kelvin
celsius = 25
kelvin = celsius + 273.15
print(f"{celsius}°C = {kelvin}K")

# Your turn: Convert 100°F to Celsius
# Write the code below:
```

### 📹 Video Resources:

1. **"Python Operators"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=v5MR5JnKcZI
   - Duration: 13 minutes
   - Covers: All operator types

2. **"Python Numbers and Math"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=khKv-8q7YmY
   - Duration: 10 minutes

3. **"Python Math Module"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=rfscVS0vtbw (timestamp 12:30)
   - Duration: 5 minutes section

### 📚 Text Resources:

1. **Python Docs - Numeric Types**
   - Link: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

2. **Real Python - Operators and Expressions**
   - Link: https://realpython.com/python-operators-expressions/

3. **W3Schools - Python Operators**
   - Link: https://www.w3schools.com/python/python_operators.asp

### ✅ Checkpoint 1:
- [✅] Understand int vs float
- [✅] Can use all arithmetic operators
- [✅] Know operator precedence
- [✅] Completed temperature converter

---

## 🕑 Session 2: Strings & String Methods (60 minutes)

### Part 2.1: String Basics

**Creating Strings:**
```python
# Single quotes
name = 'Alice'

# Double quotes
message = "Hello, World!"

# Triple quotes (multi-line)
paragraph = """This is a
multi-line string.
It can span multiple lines."""

another = '''You can also
use triple single quotes
for multi-line strings.'''

# Empty string
empty = ""

# String with quotes inside
quote1 = "She said, 'Hello!'"
quote2 = 'He said, "Goodbye!"'
quote3 = "It's a beautiful day"
quote4 = 'The book is called "Python 101"'
```

**String Concatenation:**
```python
first_name = "John"
last_name = "Doe"

# Using + operator
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Concatenation with numbers (must convert)
age = 25
# This will error:
# message = "I am " + age + " years old"  # TypeError

# Correct way:
message = "I am " + str(age) + " years old"
print(message)

# Better way: f-strings (formatted strings)
message = f"I am {age} years old"
print(message)
```

**String Indexing:**
```python
text = "Python"

# Indexing (starts at 0)
print(text[0])   # P
print(text[1])   # y
print(text[2])   # t

# Negative indexing (from the end)
print(text[-1])  # n
print(text[-2])  # o
print(text[-3])  # h

# Get length
print(len(text))  # 6
```

**String Slicing:**
```python
text = "Python Programming"

# Slicing [start:end] (end is not included)
print(text[0:6])    # Python
print(text[7:18])   # Programming

# Shortcuts
print(text[:6])     # Python (from start to index 6)
print(text[7:])     # Programming (from index 7 to end)
print(text[:])      # Python Programming (entire string)

# With step
print(text[::2])    # Pto rgamn (every 2nd character)
print(text[::-1])   # gnimmargorP nohtyP (reverse)

# Common patterns
email = "user@example.com"
username = email[:email.index('@')]  # user
domain = email[email.index('@')+1:]  # example.com
```

### Part 2.2: String Methods

**Case Methods:**
```python
text = "python programming"

print(text.upper())       # PYTHON PROGRAMMING
print(text.lower())       # python programming
print(text.capitalize())  # Python programming
print(text.title())       # Python Programming

# Checking case
print("HELLO".isupper())  # True
print("hello".islower())  # True
print("Hello".istitle())  # True
```

**String Search and Replace:**
```python
sentence = "I love Python programming. Python is awesome!"

# Find
print(sentence.find("Python"))     # 7 (first occurrence)
print(sentence.find("Java"))       # -1 (not found)
print(sentence.rfind("Python"))    # 28 (last occurrence)

# Count
print(sentence.count("Python"))    # 2

# Check if contains
print("Python" in sentence)        # True
print("Java" in sentence)          # False

# Replace
new_sentence = sentence.replace("Python", "JavaScript")
print(new_sentence)

# Replace only first occurrence
new_sentence = sentence.replace("Python", "JavaScript", 1)
print(new_sentence)
```

**String Cleaning:**
```python
text = "   Hello World   "

print(text.strip())      # "Hello World" (remove leading/trailing spaces)
print(text.lstrip())     # "Hello World   " (remove left spaces)
print(text.rstrip())     # "   Hello World" (remove right spaces)

# Remove specific characters
email = "###user@example.com###"
clean_email = email.strip('#')
print(clean_email)  # user@example.com
```

**String Split and Join:**
```python
# Split string into list
sentence = "Python is awesome"
words = sentence.split()  # Split by spaces
print(words)  # ['Python', 'is', 'awesome']

csv = "apple,banana,cherry"
fruits = csv.split(',')
print(fruits)  # ['apple', 'banana', 'cherry']

# Join list into string
words = ['Python', 'is', 'fun']
sentence = ' '.join(words)
print(sentence)  # Python is fun

fruits = ['apple', 'banana', 'cherry']
csv = ','.join(fruits)
print(csv)  # apple,banana,cherry
```

**String Validation:**
```python
# Check content type
print("hello".isalpha())      # True (only letters)
print("hello123".isalnum())   # True (letters and numbers)
print("123".isdigit())        # True (only digits)
print("   ".isspace())        # True (only whitespace)

# Practical use
password = "Pass123"
if password.isalnum() and len(password) >= 6:
    print("Valid password format")
```

**String Formatting:**
```python
name = "Alice"
age = 25
height = 5.6

# Old way (% formatting)
message = "My name is %s, I'm %d years old" % (name, age)

# New way (format method)
message = "My name is {}, I'm {} years old".format(name, age)
message = "My name is {0}, I'm {1} years old".format(name, age)
message = "My name is {n}, I'm {a} years old".format(n=name, a=age)

# Best way (f-strings - Python 3.6+)
message = f"My name is {name}, I'm {age} years old"
message = f"My height is {height:.1f} feet"  # Control decimal places
message = f"Next year I'll be {age + 1}"      # Expressions inside

# Formatting numbers
price = 19.99999
print(f"Price: ${price:.2f}")  # Price: $19.99

number = 1000000
print(f"Number: {number:,}")   # Number: 1,000,000
```

### Part 2.3: Escape Characters

```python
# Newline
print("Line 1\nLine 2")

# Tab
print("Name:\tJohn")
print("Age:\t25")

# Backslash
print("This is a backslash: \\")

# Quotes
print("She said, \"Hello!\"")
print('It\'s a nice day')

# Raw strings (ignore escape characters)
path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents
```

### Practice Exercise 2: String Manipulation

Create `string_practice.py`:
```python
# string_practice.py - String Manipulation Practice

# Exercise 1: Email extractor
email = "john.doe@example.com"
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(f"Username: {username}")
print(f"Domain: {domain}")

# Exercise 2: Name formatter
full_name = "john doe smith"
formatted = full_name.title()
print(f"Formatted: {formatted}")

# Exercise 3: Word counter
sentence = "Python is an amazing programming language"
word_count = len(sentence.split())
print(f"Word count: {word_count}")

# Exercise 4: Password validator
password = "MyPass123"
is_valid = (len(password) >= 8 and 
            any(c.isupper() for c in password) and 
            any(c.isdigit() for c in password))
print(f"Password valid: {is_valid}")

# Exercise 5: Text cleaner
text = "   Too   many   spaces   "
cleaned = ' '.join(text.split())
print(f"Cleaned: {cleaned}")
```

### 📹 Video Resources:

1. **"Python String Methods"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=k9TUPpGqYTo
   - Duration: 16 minutes

2. **"Python Strings"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=k9TUPpGqYTo
   - Duration: 12 minutes

3. **"String Formatting in Python"** by Real Python
   - Link: https://realpython.com/python-f-strings/
   - Text tutorial with examples

### 📚 Text Resources:

1. **Python Docs - String Methods**
   - Link: https://docs.python.org/3/library/stdtypes.html#string-methods

2. **W3Schools - Python Strings**
   - Link: https://www.w3schools.com/python/python_strings.asp

### ✅ Checkpoint 2:
- [ ] Can create and manipulate strings
- [ ] Know string methods (upper, lower, replace, etc.)
- [ ] Understand string slicing
- [ ] Can format strings with f-strings
- [ ] Completed string exercises

---

## 🕒 Session 3: Boolean, Comparison & Logical Operators (45 minutes)

### Part 3.1: Boolean Data Type

```python
# Boolean values
is_student = True
is_working = False

print(type(is_student))  # <class 'bool'>

# Boolean from comparisons
x = 5
y = 10
result = x < y
print(result)  # True
print(type(result))  # <class 'bool'>

# Truthy and Falsy values
# False values: False, 0, 0.0, "", [], {}, None
# Everything else is True

print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hello"))  # True
print(bool([]))       # False
print(bool([1, 2]))   # True
```

### Part 3.2: Comparison Operators

```python
x = 10
y = 5

# Equal to
print(x == y)   # False
print(5 == 5)   # True

# Not equal to
print(x != y)   # True
print(5 != 5)   # False

# Greater than
print(x > y)    # True
print(5 > 10)   # False

# Less than
print(x < y)    # False
print(5 < 10)   # True

# Greater than or equal to
print(x >= 10)  # True
print(x >= 11)  # False

# Less than or equal to
print(y <= 5)   # True
print(y <= 4)   # False

# Comparing strings (alphabetical order)
print("apple" < "banana")  # True
print("Z" < "a")           # True (uppercase comes before lowercase)
```

### Part 3.3: Logical Operators

**AND Operator:**
```python
# Both conditions must be True
age = 25
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)  # True

# Truth table for AND
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
```

**OR Operator:**
```python
# At least one condition must be True
is_weekend = True
is_holiday = False

can_relax = is_weekend or is_holiday
print(can_relax)  # True

# Truth table for OR
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

**NOT Operator:**
```python
# Reverses the boolean value
is_raining = False
is_sunny = not is_raining
print(is_sunny)  # True

# Truth table for NOT
print(not True)   # False
print(not False)  # True
```

**Combining Logical Operators:**
```python
age = 25
income = 50000
has_good_credit = True

# Complex condition
qualifies_for_loan = (age >= 21 and age <= 65) and (income >= 30000 or has_good_credit)
print(qualifies_for_loan)  # True

# Using parentheses for clarity
result = (True or False) and (True and not False)
print(result)  # True
```

### Part 3.4: Identity and Membership Operators

**Identity Operators (is, is not):**
```python
x = 5
y = 5
z = x

print(x is y)      # True (same value and same object)
print(x is not z)  # False

# Be careful with 'is' vs '=='
# 'is' checks if same object in memory
# '==' checks if same value

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same values)
print(a is b)  # False (different objects)
```

**Membership Operators (in, not in):**
```python
# Check if value exists in sequence
fruits = "apple banana cherry"

print("apple" in fruits)      # True
print("orange" in fruits)     # False
print("grape" not in fruits)  # True

# Works with strings
text = "Hello World"
print("H" in text)      # True
print("hello" in text)  # False (case-sensitive)
```

### Practice Exercise 3: Login System

Create `login_system.py`:
```python
# login_system.py - Simple Login Validator

print("=== User Login System ===\n")

# Correct credentials
correct_username = "admin"
correct_password = "pass123"

# User input (we'll use variables for now)
username = "admin"
password = "pass123"
age = 25

# Validation
valid_username = username == correct_username
valid_password = password == correct_password
is_adult = age >= 18

# Check all conditions
login_successful = valid_username and valid_password and is_adult

print(f"Valid username: {valid_username}")
print(f"Valid password: {valid_password}")
print(f"Is adult: {is_adult}")
print(f"Login successful: {login_successful}")

# Additional checks
has_special_char = "@" in password or "#" in password or "$" in password
password_length_ok = len(password) >= 6
strong_password = password_length_ok and has_special_char

print(f"\nPassword strength check:")
print(f"Length OK: {password_length_ok}")
print(f"Has special character: {has_special_char}")
print(f"Strong password: {strong_password}")
```

### 📹 Video Resources:

1. **"Boolean Logic in Python"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=DZwmZ8Usvnk
   - Duration: 10 minutes

2. **"Python Comparison and Logical Operators"** by Programming with Mosh
   - Part of larger tutorial
   - Duration: 8 minutes

### 📚 Text Resources:

1. **Python Docs - Boolean Operations**
   - Link: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

2. **Real Python - Boolean Logic**
   - Link: https://realpython.com/python-boolean/

### ✅ Checkpoint 3:
- [ ] Understand Boolean values
- [ ] Can use comparison operators
- [ ] Know logical operators (and, or, not)
- [ ] Can create complex conditions
- [ ] Completed login system exercise

---

## 🕓 Session 4: Type Conversion & User Input (45 minutes)

### Part 4.1: Type Conversion

**Converting Between Types:**
```python
# String to Integer
age_str = "25"
age_int = int(age_str)
print(age_int + 5)  # 30

# String to Float
price_str = "19.99"
price_float = float(price_str)
print(price_float * 2)  # 39.98

# Integer to String
number = 100
number_str = str(number)
print("The number is: " + number_str)

# Float to Integer (truncates decimal)
price = 19.99
price_int = int(price)
print(price_int)  # 19

# Integer to Float
age = 25
age_float = float(age)
print(age_float)  # 25.0
```

**Boolean Conversions:**
```python
# To Boolean
print(bool(1))        # True
print(bool(0))        # False
print(bool("hello"))  # True
print(bool(""))       # False

# From Boolean
print(int(True))   # 1
print(int(False))  # 0
print(str(True))   # "True"
```

**Error Handling with Conversions:**
```python
# This will cause ValueError:
# number = int("abc")  # ValueError: invalid literal

# Check before converting
text = "123"
if text.isdigit():
    number = int(text)
    print(f"Converted: {number}")
else:
    print("Cannot convert to integer")
```

### Part 4.2: User Input

**Basic Input:**
```python
# input() function always returns a string
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Get age (need to convert to int)
age_str = input("Enter your age: ")
age = int(age_str)
print(f"You are {age} years old")

# Shorter version
age = int(input("Enter your age: "))
```

**Multiple Inputs:**
```python
# Get multiple values
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))

print(f"\nProfile:")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
```

**Input with Calculations:**
```python
# Simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nResults:")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
```

### Practice Exercise 4: Interactive Programs

**Exercise A: Personal Info Collector**

Create `personal_info.py`:
```python
# personal_info.py - Collect and Display Personal Information

print("=== Personal Information Form ===\n")

# Collect information
first_name = input("First Name: ")
last_name = input("Last Name: ")
age = int(input("Age: "))
city = input("City: ")
country = input("Country: ")
email = input("Email: ")

# Calculate birth year (approximate)
current_year = 2024
birth_year = current_year - age

# Display formatted information
print("\n" + "="*40)
print("YOUR PROFILE")
print("="*40)
print(f"Name:       {first_name} {last_name}")
print(f"Age:        {age} years old")
print(f"Birth Year: {birth_year} (approx)")
print(f"Location:   {city}, {country}")
print(f"Email:      {email}")
print("="*40)

# Additional info
print(f"\nIn 10 years, you'll be {age + 10} years old!")
print(f"Your email domain is: {email.split('@')[1]}")
```

**Exercise B: BMI Calculator**

Create `bmi_calculator.py`:
```python
# bmi_calculator.py - Calculate Body Mass Index

print("=== BMI Calculator ===\n")

# Get user input
name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display results
print(f"\n{'='*40}")
print(f"BMI RESULTS FOR {name.upper()}")
print(f"{'='*40}")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI:    {bmi:.2f}")
print(f"{'='*40}")

# BMI Categories (informational)
print("\nBMI Categories:")
print("  Underweight: < 18.5")
print("  Normal:      18.5 - 24.9")
print("  Overweight:  25.0 - 29.9")
print("  Obese:       ≥ 30.0")

# Simple category check using boolean
is_underweight = bmi < 18.5
is_normal = bmi >= 18.5 and bmi < 25
is_overweight = bmi >= 25 and bmi < 30
is_obese = bmi >= 30

print(f"\nYour BMI of {bmi:.2f} indicates:")
if is_underweight:
    print("  → Underweight")
elif is_normal:
    print("  → Normal weight")
elif is_overweight:
    print("  → Overweight")
else:
    print("  → Obese")
```

**Exercise C: Shopping Receipt**

Create `shopping_receipt.py`:
```python
# shopping_receipt.py - Generate Shopping Receipt

print("=== SHOPPING RECEIPT GENERATOR ===\n")

# Get items and prices
item1 = input("Item 1 name: ")
price1 = float(input("Item 1 price: $"))

item2 = input("Item 2 name: ")
price2 = float(input("Item 2 price: $"))

item3 = input("Item 3 name: ")
price3 = float(input("Item 3 price: $"))

tax_rate = float(input("Tax rate (%): "))

# Calculations
subtotal = price1 + price2 + price3
tax = subtotal * (tax_rate / 100)
total = subtotal + tax

# Generate receipt
print("\n" + "="*40)
print("         SHOPPING RECEIPT")
print("="*40)
print(f"{item1:.<30} ${price1:>6.2f}")
print(f"{item2:.<30} ${price2:>6.2f}")
print(f"{item3:.<30} ${price3:>6.2f}")
print("-"*40)
print(f"{'Subtotal':.<30} ${subtotal:>6.2f}")
print(f"{'Tax (' + str(tax_rate) + '%)':.<30} ${tax:>6.2f}")
print("="*40)
print(f"{'TOTAL':.<30} ${total:>6.2f}")
print("="*40)
print("\nThank you for shopping with us!")
```

### 📹 Video Resources:

1. **"Python Input and Type Conversion"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=LrOAl8vUFHY
   - Duration: 8 minutes

2. **"User Input in Python"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=Dq1-OhSZU5g
   - Duration: 6 minutes

### 📚 Text Resources:

1. **Python Docs - Built-in Functions (input)**
   - Link: https://docs.python.org/3/library/functions.html#input

2. **Real Python - Type Conversion**
   - Link: https://realpython.com/python-data-types/#type-conversion

### ✅ Checkpoint 4:
- [ ] Can convert between data types
- [ ] Know how to use input()
- [ ] Can build interactive programs
- [ ] Completed all practice exercises

---

## 📝 Day 2 Summary & Achievements

### What You Mastered Today:

✅ **Numbers & Operators:**
- Integer and float data types
- All arithmetic operators (+, -, *, /, //, %, **)
- Operator precedence (PEMDAS)
- Math module functions

✅ **Strings:**
- String creation and manipulation
- String methods (upper, lower, replace, etc.)
- String slicing and indexing
- F-strings for formatting

✅ **Boolean Logic:**
- Boolean data type
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Complex conditions

✅ **Type Conversion & Input:**
- Converting between types
- Getting user input
- Building interactive programs

---

## 🎯 Assignments

### Mandatory (Complete All):
- [ ] Temperature converter with input
- [ ] String manipulation exercises
- [ ] BMI calculator
- [ ] Shopping receipt generator

### Challenge Problems:

**Challenge 1: Age Calculator**
Create a program that:
- Gets birth year from user
- Calculates current age
- Calculates age in days, hours, minutes
- Shows when user will turn 100

**Challenge 2: Password Strength Checker**
Create a program that:
- Gets password from user
- Checks length (min 8 characters)
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Rates password strength

**Challenge 3: Unit Converter**
Create a comprehensive converter for:
- Length (meters ↔ feet)
- Weight (kg ↔ pounds)
- Temperature (C ↔ F ↔ K)
- Speed (km/h ↔ mph)

---

## 📊 Self-Assessment Quiz

1. **What is the difference between / and //operators?**
   <details>
   <summary>Answer</summary>
   / returns a float, // returns an integer (floor division)
   </details>

2. **How do you concatenate strings with numbers?**
   <details>
   <summary>Answer</summary>
   Convert number to string: "Age: " + str(25) or use f-strings: f"Age: {25}"
   </details>

3. **What does the len() function do?**
   <details>
   <summary>Answer</summary>
   Returns the length (number of characters) of a string
   </details>

4. **What is the result of: True and False or True?**
   <details>
   <summary>Answer</summary>
   True (False or True = True)
   </details>

5. **How do you convert a string to an integer?**
   <details>
   <summary>Answer</summary>
   int(string_variable)
   </details>

6. **What type does input() return?**
   <details>
   <summary>Answer</summary>
   String (str)
   </details>

7. **How do you check if a substring exists in a string?**
   <details>
   <summary>Answer</summary>
   Use 'in' operator: "hello" in "hello world"
   </details>

8. **What's the difference between = and ==?**
   <details>
   <summary>Answer</summary>
   = assigns a value, == compares values
   </details>

---

## 🔗 Complete Resource List

### Video Tutorials:
1. Corey Schafer - Python Tutorial Series
2. Programming with Mosh - Python for Beginners
3. Tech With Tim - Python Basics

### Interactive Learning:
1. Python Tutor - Visualize Code
2. W3Schools - Try It Yourself
3. Programiz - Python Examples

### Documentation:
1. Python.org Official Tutorial
2. Real Python Tutorials
3. Python Docs - Built-in Types

### Practice:
1. HackerRank - Python Track
2. Codewars - Python Kata
3. LeetCode - Easy Problems

---

## 💭 Learning Journal

**Reflection Questions:**

1. What operator did you find most useful today?
   - _______________________

2. Which string method will you use most often?
   - _______________________

3. What was challenging about type conversion?
   - _______________________

4. Rate your understanding of Boolean logic (1-10):
   - _______________________

5. How many hours did you code today?
   - _______________________

6. What do you want to learn tomorrow?
   - _______________________

---

## 🚀 Git Commit & Push

Don't forget to save your work to GitHub!

```bash
# Navigate to your project folder
cd python-learning

# Add new files
git add .

# Commit with descriptive message
git commit -m "Day 2: Data types, operators, and string manipulation"

# Push to GitHub
git push
```

---

## ✅ Day 2 Completion Checklist

### Concepts Mastered:
- [ ] Integer and float data types
- [ ] All arithmetic operators
- [ ] String creation and manipulation
- [ ] String methods (5+ methods)
- [ ] String slicing and indexing
- [ ] F-strings formatting
- [ ] Boolean data type
- [ ] Comparison operators
- [ ] Logical operators (and, or, not)
- [ ] Type conversion (str, int, float)
- [ ] User input with input()

### Programs Created:
- [ ] Temperature converter
- [ ] String manipulation exercises
- [ ] Login system validator
- [ ] Personal info collector
- [ ] BMI calculator
- [ ] Shopping receipt generator
- [ ] At least 1 challenge problem

### Git & GitHub:
- [ ] All files committed
- [ ] Pushed to GitHub
- [ ] README updated with Day 2 progress

**Overall Completion: ____%**

---

## 📅 Tomorrow's Preview: Day 3

Get ready to learn:
- **Control Flow:** if, elif, else statements
- **Conditional logic**
- **Nested conditions**
- **Building decision-making programs**

See you tomorrow! 🎉

---

**Day Status:** Day 2 of 168  
**Previous:** [Day 1 - Installation & Setup](./Day_01_Complete_Guide.md)  
**Next:** [Day 3 - Control Flow](./Day_03_Complete_Guide.md)

*Keep coding! You're doing great! 💪*