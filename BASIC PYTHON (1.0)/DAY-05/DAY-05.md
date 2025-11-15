# Day 5: Functions & Modularity

**Duration:** 3-4 hours | **Date:** _________ | **Status:** ⬜ Not Started | ⬜ In Progress | ⬜ Completed

---

## 🎯 Today's Goals

By the end of today, you will:
- ✅ Understand what functions are and why they're important
- ✅ Create functions with def keyword
- ✅ Use parameters and arguments effectively
- ✅ Return values from functions
- ✅ Understand scope (local vs global variables)
- ✅ Use default parameters and keyword arguments
- ✅ Create lambda functions
- ✅ Build modular, reusable code

---

## 📋 Pre-Session Checklist

Before starting:
- [ ] Completed Days 1-4
- [ ] Understand variables and data types
- [ ] Comfortable with loops and conditionals
- [ ] Can write basic Python programs
- [ ] Have Python and VS Code ready

**Quick Review Test:**
```python
# Can you spot the repetition?
print("Hello, Alice!")
print("Welcome, Alice!")
print("Age: 25")

print("Hello, Bob!")
print("Welcome, Bob!")
print("Age: 30")

# Functions will help eliminate this repetition!
```

---

## 🕐 Session 1: Introduction to Functions (60 minutes)

### Part 1.1: What are Functions?

**Definition:**
A function is a reusable block of code that performs a specific task.

**Why Use Functions?**
1. **Code Reusability** - Write once, use many times
2. **Organization** - Break complex problems into smaller parts
3. **Maintainability** - Easier to update and debug
4. **Readability** - Makes code easier to understand

**Without Functions (Repetitive):**
```python
# Calculate area of rectangle 1
length1 = 5
width1 = 3
area1 = length1 * width1
print(f"Area 1: {area1}")

# Calculate area of rectangle 2
length2 = 8
width2 = 4
area2 = length2 * width2
print(f"Area 2: {area2}")

# Calculate area of rectangle 3
length3 = 10
width3 = 6
area3 = length3 * width3
print(f"Area 3: {area3}")
```

**With Functions (Reusable):**
```python
def calculate_area(length, width):
    area = length * width
    return area

# Use the function multiple times
area1 = calculate_area(5, 3)
area2 = calculate_area(8, 4)
area3 = calculate_area(10, 6)

print(f"Area 1: {area1}")
print(f"Area 2: {area2}")
print(f"Area 3: {area3}")
```

### Part 1.2: Creating Your First Function

**Basic Function Syntax:**
```python
def function_name():
    # Function body
    statement1
    statement2
```

**Example 1: Simple Function (No Parameters)**
```python
def greet():
    print("Hello, World!")
    print("Welcome to Python Functions!")

# Call the function
greet()
# Output:
# Hello, World!
# Welcome to Python Functions!

# You can call it multiple times
greet()
greet()
```

**Example 2: Function with Multiple Statements**
```python
def display_menu():
    print("="*40)
    print("      RESTAURANT MENU")
    print("="*40)
    print("1. Pizza - $12.99")
    print("2. Burger - $8.99")
    print("3. Salad - $6.99")
    print("="*40)

display_menu()
```

**Example 3: Function for Calculations**
```python
def print_square():
    for i in range(5):
        print("*" * 5)

print_square()
# Output:
# *****
# *****
# *****
# *****
# *****
```

### Part 1.3: Functions with Parameters

**Syntax:**
```python
def function_name(parameter1, parameter2):
    # Use parameters in function body
    statement
```

**Example 1: Single Parameter**
```python
def greet_person(name):
    print(f"Hello, {name}!")
    print(f"Welcome to Python, {name}!")

# Call with different arguments
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
```

**Example 2: Multiple Parameters**
```python
def calculate_rectangle_area(length, width):
    area = length * width
    print(f"Rectangle: {length} × {width}")
    print(f"Area: {area} square units")

calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)
```

**Example 3: Parameters in Expressions**
```python
def display_student_info(name, age, grade):
    print("="*40)
    print("STUDENT INFORMATION")
    print("="*40)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    print("="*40)

display_student_info("Alice", 15, "10th")
display_student_info("Bob", 16, "11th")
```

### Part 1.4: The return Statement

**Why Return Values?**
- Get results back from functions
- Use function output in calculations
- Chain functions together

**Basic Return Syntax:**
```python
def function_name(parameters):
    # Calculate something
    result = calculation
    return result
```

**Example 1: Simple Return**
```python
def add(a, b):
    sum = a + b
    return sum

result = add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# Use in calculations
total = add(10, 20) + add(5, 15)
print(f"Total: {total}")  # Output: Total: 50
```

**Example 2: Return Without Variable**
```python
def multiply(a, b):
    return a * b

result = multiply(4, 7)
print(result)  # Output: 28
```

**Example 3: Multiple Calculations**
```python
def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area

area = calculate_circle(5)
print(f"Circle area: {area:.2f}")
```

**Example 4: Return Multiple Values**
```python
def get_name_parts(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]
    return first_name, last_name

first, last = get_name_parts("John Michael Doe")
print(f"First: {first}")  # John
print(f"Last: {last}")    # Doe
```

**Example 5: Conditional Returns**
```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_grade(95))  # A
print(get_grade(75))  # C
print(get_grade(55))  # F
```

### Part 1.5: Function vs Procedure

**Function (Returns a value):**
```python
def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total

amount = calculate_total(100, 0.08)
print(f"Total: ${amount}")
```

**Procedure (Performs action, no return):**
```python
def display_receipt(price, tax_rate):
    total = price + (price * tax_rate)
    print("="*30)
    print("RECEIPT")
    print("="*30)
    print(f"Subtotal: ${price:.2f}")
    print(f"Tax: ${price * tax_rate:.2f}")
    print(f"Total: ${total:.2f}")
    print("="*30)

display_receipt(100, 0.08)
```

### Practice Exercise 1: Basic Functions

Create `functions_practice1.py`:
```python
# functions_practice1.py - Basic Function Practice

print("=== EXERCISE 1: Temperature Converter ===")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test the functions
c = 25
f = celsius_to_fahrenheit(c)
print(f"{c}°C = {f}°F")

f = 77
c = fahrenheit_to_celsius(f)
print(f"{f}°F = {c:.1f}°C")
print()

print("=== EXERCISE 2: BMI Calculator ===")

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)"""
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """Return BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Test
weight = 70  # kg
height = 1.75  # meters
bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")
print(f"Category: {category}")
print()

print("=== EXERCISE 3: String Utilities ===")

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def is_palindrome(text):
    """Check if string is palindrome"""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Test
word = "Python"
print(f"Original: {word}")
print(f"Reversed: {reverse_string(word)}")
print(f"Vowels: {count_vowels(word)}")

phrase = "racecar"
print(f"'{phrase}' is palindrome: {is_palindrome(phrase)}")
print()

print("=== EXERCISE 4: Math Operations ===")

def is_even(number):
    """Check if number is even"""
    return number % 2 == 0

def is_prime(number):
    """Check if number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test
print(f"10 is even: {is_even(10)}")
print(f"7 is even: {is_even(7)}")
print(f"17 is prime: {is_prime(17)}")
print(f"18 is prime: {is_prime(18)}")
print(f"5! = {factorial(5)}")
print()

print("=== EXERCISE 5: List Operations ===")

def find_max(numbers):
    """Find maximum in list"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    """Find minimum in list"""
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def calculate_average(numbers):
    """Calculate average of list"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Test
nums = [45, 23, 67, 12, 89, 34]
print(f"Numbers: {nums}")
print(f"Maximum: {find_max(nums)}")
print(f"Minimum: {find_min(nums)}")
print(f"Average: {calculate_average(nums):.2f}")
```

### 📹 Video Resources:

1. **"Python Functions"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=9Os0o3wzS_I
   - Duration: 16 minutes
   - Covers: Function basics, parameters, return values

2. **"Functions in Python"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=u-OmVr_fT4s
   - Duration: 12 minutes
   - Covers: Creating and using functions

3. **"Python Functions Tutorial"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=NSbOtYzIQI0
   - Duration: 10 minutes
   - Covers: Function fundamentals with examples

### 📚 Text Resources:

1. **Python Official Tutorial - Defining Functions**
   - Link: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
   - Official documentation with examples

2. **Real Python - Defining Functions**
   - Link: https://realpython.com/defining-your-own-python-function/
   - Comprehensive guide with best practices

3. **W3Schools - Python Functions**
   - Link: https://www.w3schools.com/python/python_functions.asp
   - Interactive examples and try-it-yourself

### ✅ Checkpoint 1:
- [ ] Understand what functions are
- [ ] Can create functions with def
- [ ] Can use parameters
- [ ] Know how to return values
- [ ] Completed basic exercises

---

## 🕑 Session 2: Advanced Function Concepts (60 minutes)

### Part 2.1: Default Parameters

**Syntax:**
```python
def function_name(param1, param2=default_value):
    # Function body
```

**Example 1: Single Default Parameter**
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                 # Uses default: Hello, Alice!
greet("Bob", "Hi")            # Custom: Hi, Bob!
greet("Charlie", "Good morning")  # Good morning, Charlie!
```

**Example 2: Multiple Default Parameters**
```python
def create_profile(name, age=18, city="Unknown", country="Unknown"):
    print("="*40)
    print("USER PROFILE")
    print("="*40)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Location: {city}, {country}")
    print("="*40)

create_profile("Alice")
create_profile("Bob", 25)
create_profile("Charlie", 30, "New York")
create_profile("Diana", 28, "London", "UK")
```

**Example 3: Calculation with Defaults**
```python
def calculate_price(base_price, tax_rate=0.08, discount=0):
    subtotal = base_price - (base_price * discount)
    total = subtotal + (subtotal * tax_rate)
    return total

print(f"${calculate_price(100):.2f}")           # Default tax, no discount
print(f"${calculate_price(100, 0.10):.2f}")    # Custom tax
print(f"${calculate_price(100, 0.08, 0.20):.2f}")  # Tax and 20% discount
```

**Important Rule:**
```python
# ✅ Correct - default parameters last
def function(a, b, c=0, d=0):
    pass

# ❌ Wrong - non-default after default
# def function(a, b=0, c, d=0):
#     pass
```

### Part 2.2: Keyword Arguments

**Positional vs Keyword Arguments:**
```python
def display_info(name, age, city):
    print(f"{name}, {age} years old, from {city}")

# Positional arguments (order matters)
display_info("Alice", 25, "New York")

# Keyword arguments (order doesn't matter)
display_info(age=25, city="New York", name="Alice")
display_info(city="Boston", name="Bob", age=30)

# Mix (positional first, then keyword)
display_info("Charlie", city="Chicago", age=28)
```

**Example: Clear Function Calls**
```python
def create_account(username, password, email, age, premium=False):
    print(f"Account created for {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"Premium: {premium}")

# Clear what each argument represents
create_account(
    username="alice123",
    password="secret",
    email="alice@example.com",
    age=25,
    premium=True
)
```

### Part 2.3: Variable-Length Arguments (*args)

**Using *args for unlimited arguments:**
```python
def add_numbers(*numbers):
    """Add any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(add_numbers(1, 2, 3))           # 6
print(add_numbers(10, 20, 30, 40))    # 100
print(add_numbers(5))                 # 5
print(add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55
```

**Example: Find Maximum**
```python
def find_maximum(*numbers):
    """Find max from any number of arguments"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_maximum(45, 23, 67, 12))   # 67
print(find_maximum(100, 200, 50))     # 200
```

**Example: Build Sentence**
```python
def build_sentence(*words):
    """Build sentence from words"""
    return " ".join(words)

print(build_sentence("Python", "is", "awesome"))
print(build_sentence("I", "love", "programming", "in", "Python"))
```

### Part 2.4: Keyword Variable Arguments (**kwargs)

**Using **kwargs for keyword arguments:**
```python
def display_info(**info):
    """Display any number of keyword arguments"""
    print("Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")

display_info(name="Alice", age=25, city="New York")
display_info(product="Laptop", price=999, brand="TechCo", warranty="2 years")
```

**Example: Create HTML Tag**
```python
def create_tag(tag_name, **attributes):
    """Create HTML tag with attributes"""
    attrs = " ".join([f'{key}="{value}"' for key, value in attributes.items()])
    return f"<{tag_name} {attrs}>"

print(create_tag("img", src="photo.jpg", alt="Photo", width="500"))
print(create_tag("a", href="https://example.com", target="_blank"))
```

**Combining *args and **kwargs:**
```python
def flexible_function(*args, **kwargs):
    """Accept any arguments"""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}
```

### Part 2.5: Scope - Local vs Global Variables

**Local Variables:**
```python
def my_function():
    x = 10  # Local variable
    print(f"Inside function: x = {x}")

my_function()
# print(x)  # Error! x doesn't exist outside function
```

**Global Variables:**
```python
x = 100  # Global variable

def my_function():
    print(f"Inside function: x = {x}")  # Can read global

my_function()
print(f"Outside function: x = {x}")
```

**Global Keyword:**
```python
count = 0  # Global

def increment():
    global count  # Modify global variable
    count += 1
    print(f"Count: {count}")

increment()  # Count: 1
increment()  # Count: 2
increment()  # Count: 3
print(f"Final count: {count}")  # Final count: 3
```

**Best Practice - Avoid globals:**
```python
# ❌ Bad - using global
total = 0
def add_to_total(value):
    global total
    total += value

# ✅ Good - pass and return
def add_to_total(current_total, value):
    return current_total + value

total = 0
total = add_to_total(total, 10)
total = add_to_total(total, 20)
```

**Scope Example:**
```python
x = "global"

def outer():
    x = "outer"
    
    def inner():
        x = "inner"
        print(f"Inner x: {x}")
    
    inner()
    print(f"Outer x: {x}")

outer()
print(f"Global x: {x}")

# Output:
# Inner x: inner
# Outer x: outer
# Global x: global
```

### Part 2.6: Docstrings

**Adding Documentation:**
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

**Good Docstring Example:**
```python
def validate_email(email):
    """
    Validate an email address.
    
    Checks if the email contains @ symbol and a domain.
    
    Args:
        email (str): The email address to validate
    
    Returns:
        bool: True if valid, False otherwise
    
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid.email")
        False
    """
    return "@" in email and "." in email.split("@")[1]
```

### Practice Exercise 2: Advanced Functions

Create `functions_practice2.py`:
```python
# functions_practice2.py - Advanced Function Practice

print("=== EXERCISE 1: Default Parameters ===")

def calculate_discount(price, discount_percent=10):
    """Calculate price after discount"""
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return final_price

print(f"$100 with default 10% discount: ${calculate_discount(100):.2f}")
print(f"$100 with 20% discount: ${calculate_discount(100, 20):.2f}")
print()

print("=== EXERCISE 2: *args Example ===")

def calculate_statistics(*numbers):
    """Calculate mean, median, min, max"""
    if not numbers:
        return None
    
    sorted_nums = sorted(numbers)
    count = len(numbers)
    
    # Mean
    mean = sum(numbers) / count
    
    # Median
    if count % 2 == 0:
        median = (sorted_nums[count//2 - 1] + sorted_nums[count//2]) / 2
    else:
        median = sorted_nums[count//2]
    
    # Min and Max
    minimum = sorted_nums[0]
    maximum = sorted_nums[-1]
    
    return {
        'mean': mean,
        'median': median,
        'min': minimum,
        'max': maximum
    }

stats = calculate_statistics(45, 23, 67, 12, 89, 34, 56)
print("Statistics:", stats)
print()

print("=== EXERCISE 3: **kwargs Example ===")

def create_user_profile(**details):
    """Create user profile from keyword arguments"""
    print("="*50)
    print("USER PROFILE")
    print("="*50)
    
    required = ['username', 'email']
    for field in required:
        if field not in details:
            return f"Error: Missing required field: {field}"
    
    for key, value in details.items():
        print(f"{key.title()}: {value}")
    print("="*50)

create_user_profile(
    username="alice123",
    email="alice@example.com",
    age=25,
    city="New York",
    premium=True
)
print()

print("=== EXERCISE 4: Scope Practice ===")

balance = 1000  # Global

def deposit(amount):
    """Deposit money - returns new balance"""
    global balance
    balance += amount
    return balance

def withdraw(amount):
    """Withdraw money - returns new balance"""
    global balance
    if amount > balance:
        print("Insufficient funds!")
        return balance
    balance -= amount
    return balance

def get_balance():
    """Get current balance"""
    return balance

print(f"Initial balance: ${get_balance()}")
deposit(500)
print(f"After deposit: ${get_balance()}")
withdraw(200)
print(f"After withdrawal: ${get_balance()}")
print()

print("=== EXERCISE 5: Recursive Function ===")

def fibonacci(n):
    """
    Calculate nth Fibonacci number.
    
    Args:
        n (int): Position in Fibonacci sequence
    
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()
```

### 📹 Video Resources:

1. **"Python Function Arguments"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=9Os0o3wzS_I
   - Duration: 13 minutes
   - Covers: Default params, *args, **kwargs

2. **"Python Variable Scope"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=QVdf0LgmICw
   - Duration: 10 minutes
   - Covers: Local, global, nonlocal

3. **"Advanced Python Functions"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=BVfCWuca9nw
   - Duration: 15 minutes

### 📚 Text Resources:

1. **Real Python - Args and Kwargs**
   - Link: https://realpython.com/python-kwargs-and-args/

2. **Python Docs - Scope and Namespaces**
   - Link: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

### ✅ Checkpoint 2:
- [ ] Understand default parameters
- [ ] Can use keyword arguments
- [ ] Know *args and **kwargs
- [ ] Understand scope
- [ ] Write docstrings

---

## 🕒 Session 3: Lambda Functions & Projects (90 minutes)

### Part 3.1: Lambda Functions

**What are Lambda Functions?**
Anonymous, one-line functions for simple operations.

**Syntax:**
```python
lambda arguments: expression
```

**Example 1: Basic Lambda**
```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square(5))          # 25
print(square_lambda(5))   # 25
```

**Example 2: Multiple Arguments**
```python
# Regular function
def add(a, b):
    return a + b

# Lambda
add_lambda = lambda a, b: a + b

print(add_lambda(3, 7))  # 10
```

**Example 3: Lambda with Conditions**
```python
# Check if number is even
is_even = lambda x: x % 2 == 0

print(is_even(10))  # True
print(is_even(7))   # False

# Get maximum
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # 20
```

**Example 4: Lambda in Sorting**
```python
# Sort by second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]

# Sort students by grade
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
sorted_students = sorted(students, key=lambda s: s['grade'], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")
```

**Example 5: Lambda with map()**
```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert to uppercase
words = ['python', 'java', 'c++']
uppercase = list(map(lambda x: x.upper(), words))
print(uppercase)  # ['PYTHON', 'JAVA', 'C++']
```

**Example 6: Lambda with filter()**
```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter long words
words = ['cat', 'elephant', 'dog', 'giraffe']
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)  # ['elephant', 'giraffe']
```

**When to Use Lambda:**
- ✅ Simple one-line operations
- ✅ Sorting with custom keys
- ✅ With map(), filter(), reduce()
- ✅ Short-lived functions

**When NOT to Use Lambda:**
- ❌ Complex logic
- ❌ Multiple statements
- ❌ Need to reuse often (use def instead)

### Project 1: Contact Manager

Create `contact_manager.py`:
```python
# contact_manager.py - Contact Management System

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("     CONTACT MANAGER")
    print("="*50)
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")
    print("="*50)

def add_contact(contacts):
    """Add a new contact"""
    print("\n--- Add New Contact ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    
    contacts.append(contact)
    print(f"✓ Contact '{name}' added successfully!")
    return contacts

def view_contacts(contacts):
    """Display all contacts"""
    if not contacts:
        print("\n❌ No contacts found!")
        return
    
    print("\n" + "="*70)
    print(f"{'Name':<20} {'Phone':<15} {'Email':<30}")
    print("="*70)
    
    for contact in contacts:
        print(f"{contact['name']:<20} {contact['phone']:<15} {contact['email']:<30}")
    print("="*70)
    print(f"Total contacts: {len(contacts)}")

def search_contact(contacts):
    """Search for a contact"""
    if not contacts:
        print("\n❌ No contacts to search!")
        return
    
    search_term = input("\nEnter name to search: ").lower()
    found = []
    
    for contact in contacts:
        if search_term in contact['name'].lower():
            found.append(contact)
    
    if found:
        print(f"\n✓ Found {len(found)} contact(s):")
        print("="*70)
        for contact in found:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-"*70)
    else:
        print(f"\n❌ No contacts found matching '{search_term}'")

def delete_contact(contacts):
    """Delete a contact"""
    if not contacts:
        print("\n❌ No contacts to delete!")
        return contacts
    
    view_contacts(contacts)
    name = input("\nEnter name of contact to delete: ")
    
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            confirm = input(f"Delete '{contact['name']}'? (yes/no): ")
            if confirm.lower() == 'yes':
                contacts.pop(i)
                print(f"✓ Contact '{name}' deleted!")
                return contacts
    
    print(f"❌ Contact '{name}' not found!")
    return contacts

def update_contact(contacts):
    """Update a contact"""
    if not contacts:
        print("\n❌ No contacts to update!")
        return contacts
    
    view_contacts(contacts)
    name = input("\nEnter name of contact to update: ")
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"\nUpdating '{contact['name']}'")
            print("(Press Enter to keep current value)")
            
            new_name = input(f"Name [{contact['name']}]: ")
            new_phone = input(f"Phone [{contact['phone']}]: ")
            new_email = input(f"Email [{contact['email']}]: ")
            
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            
            print("✓ Contact updated!")
            return contacts
    
    print(f"❌ Contact '{name}' not found!")
    return contacts

# Main program
def main():
    contacts = []
    
    while True:
        display_menu()
        choice = input("\nSelect option (1-6): ")
        
        if choice == '1':
            contacts = add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            contacts = delete_contact(contacts)
        elif choice == '5':
            contacts = update_contact(contacts)
        elif choice == '6':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid option! Please select 1-6")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### Project 2: Student Grade Manager

Create `grade_manager.py`:
```python
# grade_manager.py - Student Grade Management System

def add_student(students):
    """Add a new student"""
    name = input("Student name: ")
    
    print("Enter scores:")
    math = float(input("Math: "))
    science = float(input("Science: "))
    english = float(input("English: "))
    history = float(input("History: "))
    
    student = {
        'name': name,
        'scores': {
            'math': math,
            'science': science,
            'english': english,
            'history': history
        }
    }
    
    students.append(student)
    print(f"✓ Student '{name}' added!")
    return students

def calculate_average(scores):
    """Calculate average score"""
    return sum(scores.values()) / len(scores)

def get_grade(average):
    """Get letter grade"""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def display_student_report(student):
    """Display detailed report for one student"""
    print("\n" + "="*60)
    print(f"REPORT CARD: {student['name']}")
    print("="*60)
    
    for subject, score in student['scores'].items():
        print(f"{subject.title():<15} {score:>6.2f}")
    
    avg = calculate_average(student['scores'])
    grade = get_grade(avg)
    
    print("-"*60)
    print(f"{'Average':<15} {avg:>6.2f}")
    print(f"{'Grade':<15} {grade:>6}")
    print("="*60)

def view_all_students(students):
    """View all students with averages"""
    if not students:
        print("\n❌ No students found!")
        return
    
    print("\n" + "="*80)
    print(f"{'Name':<20} {'Math':<8} {'Science':<8} {'English':<8} {'History':<8} {'Avg':<8} {'Grade'}")
    print("="*80)
    
    for student in students:
        scores = student['scores']
        avg = calculate_average(scores)
        grade = get_grade(avg)
        
        print(f"{student['name']:<20} "
              f"{scores['math']:<8.1f} "
              f"{scores['science']:<8.1f} "
              f"{scores['english']:<8.1f} "
              f"{scores['history']:<8.1f} "
              f"{avg:<8.2f} "
              f"{grade}")
    
    print("="*80)

def get_class_statistics(students):
    """Calculate and display class statistics"""
    if not students:
        print("\n❌ No students to analyze!")
        return
    
    all_averages = [calculate_average(s['scores']) for s in students]
    
    class_avg = sum(all_averages) / len(all_averages)
    highest = max(all_averages)
    lowest = min(all_averages)
    
    # Count grades
    grades = [get_grade(avg) for avg in all_averages]
    grade_counts = {}
    for grade in grades:
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    
    print("\n" + "="*50)
    print("CLASS STATISTICS")
    print("="*50)
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Average: {highest:.2f}")
    print(f"Lowest Average: {lowest:.2f}")
    print("\nGrade Distribution:")
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = grade_counts.get(grade, 0)
        print(f"  {grade}: {count} student(s)")
    print("="*50)

def main():
    students = []
    
    while True:
        print("\n" + "="*50)
        print("     STUDENT GRADE MANAGER")
        print("="*50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Report")
        print("4. Class Statistics")
        print("5. Exit")
        print("="*50)
        
        choice = input("\nSelect option: ")
        
        if choice == '1':
            students = add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            if not students:
                print("❌ No students found!")
            else:
                name = input("Enter student name: ")
                found = False
                for student in students:
                    if student['name'].lower() == name.lower():
                        display_student_report(student)
                        found = True
                        break
                if not found:
                    print(f"❌ Student '{name}' not found!")
        elif choice == '4':
            get_class_statistics(students)
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### Project 3: Simple Bank Account System

Create `bank_system.py`:
```python
# bank_system.py - Simple Banking System with Functions

def create_account():
    """Create a new account and return account dictionary"""
    print("\n--- Create New Account ---")
    account_number = input("Account Number: ")
    name = input("Account Holder Name: ")
    initial_deposit = float(input("Initial Deposit: $"))
    pin = input("Create 4-digit PIN: ")
    
    account = {
        'account_number': account_number,
        'name': name,
        'balance': initial_deposit,
        'pin': pin,
        'transactions': [f"Initial deposit: ${initial_deposit:.2f}"]
    }
    
    print(f"\n✓ Account created for {name}!")
    return account

def verify_pin(account):
    """Verify PIN for account access"""
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter PIN: ")
        if entered_pin == account['pin']:
            return True
        attempts -= 1
        if attempts > 0:
            print(f"❌ Incorrect PIN! {attempts} attempts remaining")
    print("❌ Account locked due to too many failed attempts!")
    return False

def check_balance(account):
    """Display account balance"""
    print("\n" + "="*40)
    print("ACCOUNT BALANCE")
    print("="*40)
    print(f"Account: {account['account_number']}")
    print(f"Holder: {account['name']}")
    print(f"Balance: ${account['balance']:.2f}")
    print("="*40)

def deposit(account):
    """Deposit money into account"""
    amount = float(input("Deposit amount: $"))
    
    if amount <= 0:
        print("❌ Amount must be positive!")
        return account
    
    account['balance'] += amount
    account['transactions'].append(f"Deposit: +${amount:.2f}")
    print(f"\n✓ ${amount:.2f} deposited successfully!")
    print(f"New balance: ${account['balance']:.2f}")
    return account

def withdraw(account):
    """Withdraw money from account"""
    amount = float(input("Withdrawal amount: $"))
    
    if amount <= 0:
        print("❌ Amount must be positive!")
        return account
    
    if amount > account['balance']:
        print(f"❌ Insufficient funds!")
        print(f"Available balance: ${account['balance']:.2f}")
        return account
    
    # Check daily withdrawal limit
    daily_limit = 1000
    if amount > daily_limit:
        print(f"❌ Daily withdrawal limit is ${daily_limit:.2f}")
        return account
    
    account['balance'] -= amount
    account['transactions'].append(f"Withdrawal: -${amount:.2f}")
    print(f"\n✓ ${amount:.2f} withdrawn successfully!")
    print(f"Remaining balance: ${account['balance']:.2f}")
    return account

def transfer(account, all_accounts):
    """Transfer money to another account"""
    to_account_num = input("Transfer to account number: ")
    
    # Find recipient account
    recipient = None
    for acc in all_accounts:
        if acc['account_number'] == to_account_num:
            recipient = acc
            break
    
    if not recipient:
        print(f"❌ Account {to_account_num} not found!")
        return account, all_accounts
    
    if recipient['account_number'] == account['account_number']:
        print("❌ Cannot transfer to same account!")
        return account, all_accounts
    
    amount = float(input("Transfer amount: $"))
    
    if amount <= 0:
        print("❌ Amount must be positive!")
        return account, all_accounts
    
    if amount > account['balance']:
        print(f"❌ Insufficient funds!")
        return account, all_accounts
    
    # Perform transfer
    account['balance'] -= amount
    recipient['balance'] += amount
    
    account['transactions'].append(f"Transfer to {to_account_num}: -${amount:.2f}")
    recipient['transactions'].append(f"Transfer from {account['account_number']}: +${amount:.2f}")
    
    print(f"\n✓ ${amount:.2f} transferred to {recipient['name']}!")
    print(f"Remaining balance: ${account['balance']:.2f}")
    
    return account, all_accounts

def view_transactions(account):
    """Display transaction history"""
    print("\n" + "="*50)
    print(f"TRANSACTION HISTORY - {account['name']}")
    print("="*50)
    
    if not account['transactions']:
        print("No transactions yet.")
    else:
        for i, transaction in enumerate(account['transactions'], 1):
            print(f"{i}. {transaction}")
    
    print("="*50)

def calculate_interest(account, rate=0.05):
    """Calculate and add interest to account"""
    interest = account['balance'] * rate
    account['balance'] += interest
    account['transactions'].append(f"Interest: +${interest:.2f}")
    print(f"\n✓ Interest of ${interest:.2f} added!")
    return account

def main():
    accounts = []
    current_account = None
    
    while True:
        if current_account is None:
            # Main menu (not logged in)
            print("\n" + "="*50)
            print("     WELCOME TO PYTHON BANK")
            print("="*50)
            print("1. Create Account")
            print("2. Login to Account")
            print("3. Exit")
            print("="*50)
            
            choice = input("\nSelect option: ")
            
            if choice == '1':
                account = create_account()
                accounts.append(account)
            
            elif choice == '2':
                if not accounts:
                    print("❌ No accounts exist! Create an account first.")
                    continue
                
                acc_num = input("Account Number: ")
                found = False
                for account in accounts:
                    if account['account_number'] == acc_num:
                        if verify_pin(account):
                            current_account = account
                            print(f"\n✓ Welcome, {account['name']}!")
                        found = True
                        break
                
                if not found:
                    print("❌ Account not found!")
            
            elif choice == '3':
                print("\n👋 Thank you for banking with us!")
                break
            
            else:
                print("❌ Invalid option!")
        
        else:
            # Account menu (logged in)
            print("\n" + "="*50)
            print(f"     {current_account['name']}'s Account")
            print("="*50)
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Transaction History")
            print("6. Logout")
            print("="*50)
            
            choice = input("\nSelect option: ")
            
            if choice == '1':
                check_balance(current_account)
            elif choice == '2':
                current_account = deposit(current_account)
            elif choice == '3':
                current_account = withdraw(current_account)
            elif choice == '4':
                current_account, accounts = transfer(current_account, accounts)
            elif choice == '5':
                view_transactions(current_account)
            elif choice == '6':
                print(f"\n👋 Goodbye, {current_account['name']}!")
                current_account = None
            else:
                print("❌ Invalid option!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### Practice Exercise 3: Lambda Functions

Create `lambda_practice.py`:
```python
# lambda_practice.py - Lambda Function Practice

print("=== EXERCISE 1: Basic Lambda ===")

# Square function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Cube function
cube = lambda x: x ** 3
print(f"Cube of 4: {cube(4)}")

# Check if even
is_even = lambda x: x % 2 == 0
print(f"10 is even: {is_even(10)}")
print()

print("=== EXERCISE 2: Lambda with map() ===")

numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print()

print("=== EXERCISE 3: Lambda with filter() ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Filter numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")
print()

print("=== EXERCISE 4: Lambda with sorted() ===")

# Sort by length
words = ['python', 'java', 'c', 'javascript', 'go']
sorted_words = sorted(words, key=lambda x: len(x))
print(f"Sorted by length: {sorted_words}")

# Sort students by grade
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
sorted_students = sorted(students, key=lambda s: s['grade'], reverse=True)
print("\nSorted by grade:")
for student in sorted_students:
    print(f"  {student['name']}: {student['grade']}")
```

### 📹 Video Resources:

1. **"Python Lambda Functions"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=25ovCm9jKfA
   - Duration: 11 minutes

2. **"Map, Filter, Lambda"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=cKlnR-CB3tk
   - Duration: 8 minutes

### 📚 Text Resources:

1. **Real Python - Lambda Functions**
   - Link: https://realpython.com/python-lambda/

2. **Python Docs - Lambda**
   - Link: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

### ✅ Checkpoint 3:
- [ ] Understand lambda syntax
- [ ] Can use lambda with map/filter
- [ ] Built all 3 projects
- [ ] Projects working correctly
- [ ] Code well-documented

---

## 📝 Day 5 Summary & Achievements

### What You Mastered Today:

✅ **Function Basics:**
- Defining functions with def
- Parameters and arguments
- Return statements
- Function vs procedure

✅ **Advanced Concepts:**
- Default parameters
- Keyword arguments
- *args and **kwargs
- Variable scope
- Docstrings

✅ **Lambda Functions:**
- Anonymous functions
- map(), filter(), sorted()
- When to use lambda

✅ **Projects Completed:**
- Contact manager
- Grade management system
- Banking system

---

## 🎯 Day 5 Assignments

### Mandatory:
- [ ] Complete all practice exercises
- [ ] Build all 3 projects
- [ ] Understand scope fully
- [ ] Write docstrings
- [ ] Push to GitHub

### Challenge Problems:

**Challenge 1: Library Management**
- Add/remove books
- Search by title/author
- Check out/return books
- Track due dates
- Late fees calculation

**Challenge 2: To-Do List Manager**
- Add tasks with priority
- Mark complete/incomplete
- Filter by priority/status
- Save to file
- Load from file

**Challenge 3: Scientific Calculator**
- Basic operations (+, -, *, /)
- Advanced (sin, cos, log, sqrt)
- History of calculations
- Unit conversion
- Statistical functions

---

## 📊 Self-Assessment Quiz

1. What's the difference between parameters and arguments?
<details>
<summary>Answer</summary>
Parameters are variables in function definition; arguments are actual values passed when calling
</details>

2. What does this return?
```python
def mystery(x, y=5):
    return x + y
print(mystery(3))
```
<details>
<summary>Answer</summary>
8 (uses default y=5)
</details>

3. What's wrong with this?
```python
def func(a=1, b):
    return a + b
```
<details>
<summary>Answer</summary>
Default parameters must come after non-default
</details>

4. When should you use lambda?
<details>
<summary>Answer</summary>
For simple one-line operations, especially with map/filter/sorted
</details>

5. What's the output?
```python
x = 10
def func():
    x = 5
func()
print(x)
```
<details>
<summary>Answer</summary>
10 (local x doesn't affect global)
</details>

---

## 💡 Function Best Practices

1. **Single Responsibility**
   - One function, one task
   - Makes testing easier
   - Improves reusability

2. **Descriptive Names**
   ```python
   # ✅ Good
   def calculate_total_price(items):
       pass
   
   # ❌ Bad
   def calc(x):
       pass
   ```

3. **Keep It Short**
   - Max 20-30 lines
   - Extract complex logic
   - Use helper functions

4. **Use Docstrings**
   ```python
   def greet(name):
       """Greet a person by name"""
       return f"Hello, {name}!"
   ```

5. **Avoid Side Effects**
   ```python
   # ✅ Good - returns new value
   def add(a, b):
       return a + b
   
   # ❌ Bad - modifies global
   total = 0
   def add(value):
       global total
       total += value
   ```

---

## 🚀 Git Commit & Push

```bash
git add .
git commit -m "Day 5: Functions, lambda, and 3 major projects"
git push
```

---

## ✅ Day 5 Completion Checklist

### Concepts:
- [ ] Function definition
- [ ] Parameters/arguments
- [ ] Return values
- [ ] Default parameters
- [ ] Keyword arguments
- [ ] *args, **kwargs
- [ ] Scope (local/global)
- [ ] Lambda functions
- [ ] Docstrings

### Projects:
- [ ] Contact manager
- [ ] Grade manager
- [ ] Bank system
- [ ] 1+ challenge

### Quality:
- [ ] Functions documented
- [ ] No global variables
- [ ] Clean code
- [ ] Tested thoroughly

**Overall: ____%**

---

## 📅 Tomorrow's Preview: Day 6

- **Lists and Tuples**
- **List methods**
- **List comprehensions**
- **Sorting and searching**

---

## 💭 Learning Journal

1. Favorite function concept?
   - _______________________

2. Most challenging project?
   - _______________________

3. Lambda understanding (1-10)?
   - _______________________

4. Hours coded today?
   - _______________________

---

## 🔗 Resources

- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python - Functions](https://realpython.com/defining-your-own-python-function/)
- [Corey Schafer - Functions](https://www.youtube.com/watch?v=9Os0o3wzS_I)

---

**Day 5 of 168 Complete!** 🎉

*"Functions are the building blocks of reusable code."*